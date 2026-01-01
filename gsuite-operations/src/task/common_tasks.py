#!/usr/bin/env python

import gspread
from gspread.exceptions import *
from gspread_formatting import *

from pprint import pprint

from task import *
from helper.utils import *
from helper.logger import *
from helper.data import *

''' create worksheet *-new-toc* from *-toc* worksheet
'''
def new_toc_from_toc(gsheet):
    # duplicate the *-toc* as *-toc-new* worksheet
    toc_ws_name = '-toc'
    toc_new_ws_name = '-toc-new'
    gsheet.duplicate_worksheet(worksheet_name_to_duplicate=toc_ws_name, new_worksheet_names=[toc_new_ws_name])

    # get the -toc-new worksheet
    toc_new_ws = gsheet.worksheet_by_name(toc_new_ws_name)
    if toc_new_ws is None:
        return

    requests = []

    gsheet.clear_conditional_formats(worksheet_names=['toc_new_ws_name'])

    # unhide all columns
    requests = requests + toc_new_ws.column_unhide_requests()

    # if there are 20 columns in -toc-new, insert three columns at position 16 (Q) (override-header, override-footer, backgrounf-image)
    if (toc_new_ws.col_count() == 20):
        requests = requests + toc_new_ws.dimension_add_requests(cols_to_add_at='Q', cols_to_add=3)


    # add 3 new columns after G - 'landscape', 'page-spec', 'margin-spec'. Column G we will use for 'break'
    requests = requests + toc_new_ws.dimension_add_requests(cols_to_add_at='H', cols_to_add=3)

    WORKSHEET_SPEC = WORKSHEET_STRUCTURE['-toc-new']


    #  resize columns
    requests = requests + toc_new_ws.column_resize_requests(WORKSHEET_SPEC['columns'])


    # batch the requests
    gsheet.update_in_batch(values=[], requests=requests)


    # for each column
    range_work_specs = {}
    requests = []
    info(f"generating .. dynamic ranges", nesting_level=1)
    for col_a1, col_data in WORKSHEET_SPEC['columns'].items():
        # change the labels in row 2
        if ('label' in col_data):
            range_spec = f"{col_a1}2"
            range_work_specs[range_spec] = {'value': col_data['label']}

        # set horizontal alignments
        if ('halign' in col_data):
            range_spec = f"{col_a1}:{col_a1}"
            range_work_specs[range_spec] = {'halign': col_data['halign']}

        # set validation rules
        range_spec = f"{col_a1}3:{col_a1}"
        requests = requests + toc_new_ws.data_validation_clear_requests(range_spec)
        if ('validation-list' in col_data):
            requests = requests + toc_new_ws.data_validation_from_list_requests(range_spec, col_data['validation-list'])


    # get the work range requests
    values, formats = toc_new_ws.range_work_requests(range_work_specs=range_work_specs)
    requests = requests + formats


    range_spec = 'C3:V'
    vals_list = toc_new_ws.get_values_in_batch(ranges=[range_spec], major_dimension='ROWS')
    for row in vals_list[0]:
        row_len = len(row)

        # for column C (process) (range C3:C), change values to blank if it is -
        col_idx = LETTER_TO_COLUMN['C'] - 3
        if (col_idx < row_len):
            if (row[col_idx] == '-'):
                row[col_idx] = ''

        # for column I (page-spec) (range I3:I), change values to A4
        col_idx = LETTER_TO_COLUMN['I'] - 3
        if (col_idx < row_len):
            row[col_idx] = 'A4'


        # for column J (margin-spec) (range J3:J), change values to narrow
        col_idx = LETTER_TO_COLUMN['J'] - 3
        if (col_idx < row_len):
            row[col_idx] = 'narrow'

        # for column K (hide-pageno) (range K3:K), change values to Yes if it is No
        col_idx = LETTER_TO_COLUMN['K'] - 3
        if (col_idx < row_len):
            if (row[col_idx] == '-'):
                row[col_idx] = ''
            elif (row[col_idx] == 'No'):
                row[col_idx] = 'Yes'


        # for column L (hide-heading) (range L3:L), change values to blank if it is -
        col_idx = LETTER_TO_COLUMN['L'] - 3
        if (col_idx < row_len):
            if (row[col_idx] == '-'):
                row[col_idx] = ''

        # for column M (different-firstpage) (range M3:M), change values to blank if it is -
        col_idx = LETTER_TO_COLUMN['M'] - 3
        if (col_idx < row_len):
            if (row[col_idx] == '-'):
                row[col_idx] = ''

        # for column T (override-header) (range T3:T), change values to blank if it is -
        col_idx = LETTER_TO_COLUMN['T'] - 3
        if (col_idx < row_len):
            if (row[col_idx] == '-'):
                row[col_idx] = ''

        # for column U (override-footer) (range U3:U), change values to blank if it is -
        col_idx = LETTER_TO_COLUMN['U'] - 3
        if (col_idx < row_len):
            if (row[col_idx] == '-'):
                row[col_idx] = ''

        # for column H (landscape) (range H3:H), change values to Yes if column G contains landscape
        # for column G (break) (range G3:G), change values to blank if it is -, change to section if it contains newpage
        col_idx_g = LETTER_TO_COLUMN['G'] - 3
        col_idx_h = LETTER_TO_COLUMN['H'] - 3
        if (col_idx_h < row_len):
            if (row[col_idx_g] == '-'):
                row[col_idx_g] = ''

            elif (row[col_idx_g].endswith('_landscape')):
                row[col_idx_h] = 'Yes'

            if (row[col_idx_g].startswith('newpage_')):
                row[col_idx_g] = 'section'

            if (row[col_idx_g].startswith('continuous_')):
                row[col_idx_g] = ''


    values.append({'range': range_spec, 'values': vals_list})

    # clear conditional formatting
    requests = requests + toc_new_ws.conditional_formatting_rules_clear_requests()

    # conditional formatting for blank cells
    requests = requests + toc_new_ws.conditional_formatting_for_blank_cells_requests(WORKSHEET_SPEC['cell-empty-markers'])

    #  freeze rows and columns
    requests = requests + toc_new_ws.dimension_freeze_requests(frozen_rows=WORKSHEET_SPEC['frozen-rows'], frozen_cols=WORKSHEET_SPEC['frozen-columns'])


    value_count = len(values)
    format_count = len(requests)

    info(f"generated  .. {value_count} dynamic values", nesting_level=1)
    info(f"generated  .. {format_count} dynamic formats", nesting_level=1)

    info(f"formatting .. ranges", nesting_level=1)
    gsheet.update_in_batch(values=values, requests=requests)
    info(f"formatted  .. {format_count} ranges", nesting_level=1)
    info(f"updated    .. {value_count} ranges", nesting_level=1)



''' adhoc task
'''
def insert_a_row_with_values(g_sheet):
    worksheet = g_sheet.worksheet_by_name(worksheet_name='01-summary')
    if not worksheet:
        return False

    # insert row at 7
    requests = worksheet.dimension_add_request(rows_to_add_at=7, rows_to_add=1)

    # B8 will be Address
    range_work_specs = {'B8': {'value': 'Address'}}
    values, _ = worksheet.range_work_request(range_work_specs=range_work_specs)

    g_sheet.update_in_batch(request_list=requests)
    worksheet.update_values_in_batch(values=values)



''' adhoc task
'''
def populate_range(g_sheet):
    worksheet = g_sheet.worksheet_by_name(worksheet_name='-toc-new')
    if not worksheet:
        return False

    # range O3:O to be z-header and linked, range R3:R to be z-footer and linked
    worksheet_dict = g_sheet.worksheets_as_dict()
    values = []
    num_rows, _ = worksheet.number_of_dimesnions()
    for row_num in range(4, num_rows+1):
        values.append({'range': f"O{row_num}", 'values': [[build_value_from_work_spec(work_spec={'value': 'z-header', 'ws-name-to-link': 'z-header'}, worksheet_dict=worksheet_dict)]]})
        values.append({'range': f"R{row_num}", 'values': [[build_value_from_work_spec(work_spec={'value': 'z-footer', 'ws-name-to-link': 'z-footer'}, worksheet_dict=worksheet_dict)]]})

    if len(values):
        worksheet.update_values_in_batch(values=values)



''' web image links (image formula) to drive file links
    this is because we are moving all artifacts (photo, signature, nid, certificates) to Google drive from of web/ftp
'''
def web_image_to_drive_file_link_for_artifacts(g_sheet, g_service, worksheet_names=[], worksheet_names_excluded=[], nesting_level=0):
    folders_by_organization = {
        '01-spectrum': '12mbhWHu3SgcUOXcdINVAf6z8vEN5DGM6',
        '02-sscl': '1xbkBeWsuMrUIFQmd5MpzLTRIMaL5KOEa',
        '03-doer': '10JCJYypX2KtVHz_t4kxXfxUNghNtg9Gx',
        '01-celloscope': '1nlzGWA6H_tzYcaGDZt7qLuMvznvxSpUu',
        '05-ael': '15VOhVeIyKEn3rtpithUYlsuzKXFczLWP',
        '06-external': '1LNlrmJ3f1rgOlAJAdaF4VpCvps0zc5NV',
    }

    image_formula_pattern = r'=image\("https://spectrum-bd.biz/data/artifacts[/]+(?P<artifact_type>.+?)[/]+(?P<organization>.+?)[/]+(?P<image_string>.+?)".+\)'

    value_requests = []
    matching_worksheet_names = g_sheet.matching_worksheet_names(worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded, nesting_level=nesting_level+1)
    for worksheet_name in matching_worksheet_names:
        ws = g_sheet.worksheet_by_name(worksheet_name=worksheet_name, nesting_level=nesting_level+1)
        if ws is None:
            warn(f"[{worksheet_name}] NOT FOUND .. ignoring ..", nesting_level=nesting_level)
            continue

        trace(f"[{worksheet_name:30}] - searching for images", nesting_level=nesting_level)

        ws_id = ws.id
        range_spec = f"'{worksheet_name}'!B3:Z"
        response = g_sheet.get_range_values_in_batch(range_spec=range_spec, valueRenderOption='FORMULA', requester='web_image_to_drive_file_link_for_artifacts', nesting_level=nesting_level+1)
        if response is None:
            continue

        if 'valueRanges' not in response:
            continue

        values = response['valueRanges'][0]

        image_formula_cells = []
        for r, row in enumerate(values.get('values', []), start=3):
            for c, col in enumerate(row, start=2):
                cell_a1 = f"{COLUMN_TO_LETTER[c]}{r}"
                m = re.match(image_formula_pattern, str(col), re.IGNORECASE)
                if m:
                    trace(f"match in [{cell_a1}] : {col}", nesting_level=nesting_level+1)
                    if m.group('organization') is not None:
                        organization = m.group('organization')
                    else:
                        warn(f"[{cell_a1}] - [{col}] organization could not be found in the formula", nesting_level=nesting_level+1)
                        continue

                    if m.group('artifact_type') is not None:
                        artifact_type = m.group('artifact_type')
                        if artifact_type in ['res'] and organization in ['logo']:
                            # ignore
                            warn(f"{cell_a1} is a LOGO .. ignoring ..", nesting_level=nesting_level+1)
                            continue
                    else:
                        warn(f"[{cell_a1}] - [{col}] artifact type could not be found in the formula", nesting_level=nesting_level+1)
                        continue

                    if m.group('image_string') is not None:
                        image_string = m.group('image_string')
                    else:
                        warn(f"[{cell_a1}] - [{col}] image string could not be found in the formula", nesting_level=nesting_level+1)
                        continue

                    image_string = cleanup_url(image_string.split('/')[-1])
                    image_formula_cells.append({'worksheet_name': worksheet_name, 'ws_id':  ws_id, 'cell_a1': cell_a1, 'organization': organization, 'artifact_type': artifact_type, 'image_string': image_string })


        cell_requests = {}
        # iterate over the image cells 
        for i, image_cell in enumerate(image_formula_cells, start=1):
            # we are to convert the formula to a hyperlink formula so that drive images are accounted for, get the drive link for the image 
            # image_drive_link = g_service.get_drive_file(drive_file_name=image_cell['image_string'], folder_id=folders_by_organization.get(image_cell['organization']), nesting_level=nesting_level+1)
            image_drive_link = g_service.get_drive_file(drive_file_name=image_cell['image_string'], folder_id=None, nesting_level=nesting_level+1)
            if image_drive_link is None:
                warn(f"{image_cell['image_string']} NOT FOUND ...", nesting_level=nesting_level+1)
                continue

            # build the new formula
            new_cell_formula = f'=HYPERLINK("{image_drive_link['webViewLink']}", "{image_cell['image_string']}")'

            # build request for cell value change
            cell_requests[image_cell['cell_a1']] = {'value': new_cell_formula}

        # process the work-specs
        vals, _ = ws.range_work_requests(range_work_specs=cell_requests, worksheets_dict={}, nesting_level=nesting_level+1)
        value_requests = value_requests + vals

        if len(vals):
            debug(f"[{worksheet_name:30}] - {len(vals)} values will be changed", nesting_level=nesting_level)

    # execute the requests for all worksheets in batch
    value_results = g_sheet.update_values_in_batch(value_list=value_requests, requester='web_image_to_drive_file_link_for_artifacts', nesting_level=nesting_level+1)
