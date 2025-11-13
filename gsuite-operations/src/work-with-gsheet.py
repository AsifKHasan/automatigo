#!/usr/bin/env python

import json
import yaml
import time
import argparse

from ggle.google_service import GoogleService

from helper.logger import *
from helper import logger
from helper.utils import *

from task.common_tasks import *
from task.resume_tasks import *

final_list = []

def execute_gsheet_tasks(g_sheet, g_service, gsheet_tasks=[], worksheet_names=[], worksheet_names_excluded=[], destination_gsheet_names=[], work_specs={}, find_replace_patterns=[], worksheet_defs={}):
    for gsheet_task_def in gsheet_tasks:
        task_name = gsheet_task_def['task']
        if hasattr(g_sheet, task_name) and callable(getattr(g_sheet, task_name)):
            match_worksheet_names = gsheet_task_def.get('match_worksheet_names', True)

            # arguments
            args_dict = {}
            for k, v in gsheet_task_def.items():
                if k == 'task':
                    pass

                elif k == 'worksheet_names' and v == True:
                    if match_worksheet_names:
                        args_dict[k] = g_sheet.matching_worksheet_names(worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded)
                    else:
                        args_dict[k] = worksheet_names

                elif k == 'destination_gsheet_names' and v == True:
                    args_dict[k] = destination_gsheet_names

                elif k == 'work_specs' and v == True:
                    args_dict[k] = work_specs

                elif k == 'find_replace_patterns' and v == True:
                    args_dict[k] = find_replace_patterns

                elif k == 'worksheet_defs' and v == True:
                    args_dict[k] = worksheet_defs

                else:
                    args_dict[k] = v

            # matching_worksheet_names argument is not to be passed
            args_dict.pop('match_worksheet_names', None)


            # execute the task
            try:
                task = getattr(g_sheet, task_name)
                info(f"executing task [{task_name}]")

                if 'worksheet_names' in args_dict:
                    debug(f"worksheets to work on {args_dict['worksheet_names']}")
                    for x in args_dict['worksheet_names']:
                        trace(f".. {x}")

                task(**args_dict)
                debug(f"executed  task [{task_name}]")
            except Exception as e:
                error(str(e))

        else:
            error(f"g_sheet has no method [{task_name}]")



def work_on_gsheet(g_sheet, g_service, worksheet_names=[], destination_gsheet_names=[], work_specs={}, find_replace_patterns=[]):
    folders_by_organization = {
        '01-spectrum': '12mbhWHu3SgcUOXcdINVAf6z8vEN5DGM6',
        '02-sscl': '1xbkBeWsuMrUIFQmd5MpzLTRIMaL5KOEa',
        '03-doer': '10JCJYypX2KtVHz_t4kxXfxUNghNtg9Gx',
        '01-celloscope': '1nlzGWA6H_tzYcaGDZt7qLuMvznvxSpUu',
        '05-ael': '15VOhVeIyKEn3rtpithUYlsuzKXFczLWP',
        '06-external': '1LNlrmJ3f1rgOlAJAdaF4VpCvps0zc5NV',
    }

    g_drive = GoogleDrive(google_service=g_service, google_drive=g_service.drive_service)
    image_formula_pattern = r'=image\("https://spectrum-bd.biz/data/artifacts/(?P<artifact_type>.+?)/(?P<organization>.+?)/(?P<image_string>.+?)".+\)'

    value_requests = []
    for worksheet_name in worksheet_names:
        ws = g_sheet.worksheet_by_name(worksheet_name=worksheet_name)
        if ws is None:
            warn(f"[{worksheet_name}] NOT FOUND .. ignoring ..")
            continue

        ws_id = ws.id
        range_spec = f"'{worksheet_name}'!B3:Z"
        values = g_sheet.get_range_values(range_spec=range_spec, valueRenderOption='FORMULA')
        image_formula_cells = []
        for r, row in enumerate(values.get('values', []), start=3):
            for c, col in enumerate(row, start=2):
                cell_a1 = f"{COLUMN_TO_LETTER[c]}{r}"
                m = re.match(image_formula_pattern, str(col), re.IGNORECASE)
                if m:
                    if m.group('artifact_type') is not None:
                        artifact_type = m.group('artifact_type')
                        if artifact_type in ['logo']:
                            # ignore
                            warn(f"{cell_a1} is a LOGO .. ignoring ..")
                            continue
                    else:
                        warn(f"[{cell_a1}] - [{col}] artifact type could not be found in the formula")
                        continue

                    if m.group('organization') is not None:
                        organization = m.group('organization')
                    else:
                        warn(f"[{cell_a1}] - [{col}] organization could not be found in the formula")
                        continue

                    if m.group('image_string') is not None:
                        image_string = m.group('image_string')
                    else:
                        warn(f"[{cell_a1}] - [{col}] image string could not be found in the formula")
                        continue

                    image_string = cleanup_url(image_string.split('/')[-1])
                    image_formula_cells.append({'worksheet_name': worksheet_name, 'ws_id':  ws_id, 'cell_a1': cell_a1, 'organization': organization, 'artifact_type': artifact_type, 'image_string': image_string })
                    # print(f"['{worksheet_name}'!{cell_a1}] - organization = [{organization}], artifact_type = [{artifact_type}], image_string = [{image_string}]")
                    # print(f"['{worksheet_name}'!{cell_a1}] - image_string = [{image_string}]")


        cell_requests = {}
        # iterate over the image cells 
        for i, image_cell in enumerate(image_formula_cells, start=1):
            # we are to convert the formula to a hyperlink formula so that drive images are accounted for, get the drive link for the image 
            # image_drive_link = g_drive.get_drive_file(drive_file_name=image_cell['image_string'], folder_id=folders_by_organization.get(image_cell['organization']))
            image_drive_link = g_drive.get_drive_file(drive_file_name=image_cell['image_string'], folder_id=None)
            if image_drive_link is None:
                warn(f"{image_cell['image_string']} NOT FOUND ...")
                continue

            # build the new formula
            new_cell_formula = f'=HYPERLINK("{image_drive_link['webViewLink']}", "{image_cell['image_string']}")'

            # build request for cell value change
            cell_requests[image_cell['cell_a1']] = {'value': new_cell_formula}

        # store the work_specs
        vals, _ = ws.range_work_requests(range_work_specs=cell_requests, worksheets_dict={})
        value_requests = value_requests + vals
        debug(f"[{worksheet_name:30}] - {len(vals)} values to be changed")

    # execute the requests for all worksheets in batch
    value_results = g_sheet.update_values_in_batch(value_list=value_requests, requester='work_on_gsheet')


    # BEGIN common tasks
    # new_toc_from_toc(g_sheet)
    # END   common tasks

    # BEGIN adhoc tasks
    # populate_range(g_sheet=g_sheet)
    # insert_a_row_with_values(g_sheet=g_sheet)
    # END   adhoc tasks

    # BEGIN resume specific tasks
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=['02-career-highlight'], range_spec='B3:Z', grouping_columns=1)
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=['04-managerial-expertise', '05-technical-expertise'], range_spec='B4:Z', grouping_columns=1)
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=['06-job-history', '07-project-roles', '07-project-roles-RHD-TMC'], range_spec='B4:Z', grouping_columns=2)
    # END   resume specific tasks

    # BEGIN PDS specific tasks
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=['06-description', '07-functionality', '08-technology', '09-services', '10-process'], range_spec='B3:Z', grouping_columns=1)
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=['05-people'], range_spec='B3:Z', grouping_columns=2)
    # END   PDS specific tasks

    # BEGIN drive/file related
    # g_sheet.share(email='asif.hasan@gmail.com', perm_type='user', role='owner')
    # END   drive/file related

    pass



if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-g", "--gsheet", required=False, help="gsheet name to work with", default=argparse.SUPPRESS)
    args = vars(ap.parse_args())

    # read config.yml to get the list of gsheets and other data
    config = yaml.load(open('../conf/data.yml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    logger.LOG_LEVEL = config.get('log-level', 0)

    # first we check whether the gsheet argument was passed or not
    if 'gsheet' in args and args["gsheet"] != '':
        gsheet_names = [args["gsheet"]]
    else:
        gsheet_names = config['gsheets']

    credential_json = config['credential-json']

    destination_gsheet_names = config.get('destination-gsheet-names', [])
    if destination_gsheet_names is None: destination_gsheet_names = []

    gsheet_tasks = config.get('gsheet-tasks', [])
    if gsheet_tasks is None: gsheet_tasks = []

    worksheet_names = config.get('worksheet-names', [])
    if worksheet_names is None: worksheet_names = []

    worksheet_names_excluded = config.get('worksheet-names-excluded', [])
    if worksheet_names_excluded is None: worksheet_names_excluded = []

    work_specs = config.get('work-specs', {})

    find_replace_patterns = config.get('find-replace-patterns', [])
    if find_replace_patterns is None: find_replace_patterns = []

    worksheet_defs = config.get('worksheet-defs', {})
    if worksheet_defs is None: worksheet_defs = {}

    g_service = GoogleService(credential_json)

    wait_for = 30
    num_gsheets = len(gsheet_names)
    for count, gsheet_name in enumerate(gsheet_names, start=1):
        try:
            info(f"processing {count:>4}/{num_gsheets} gsheet {gsheet_name}")
            g_sheet = g_service.open_gsheet(gsheet_name=gsheet_name)
        except Exception as e:
            g_sheet = None
            warn(str(e))
            # raise e

        if g_sheet:
            execute_gsheet_tasks(g_sheet=g_sheet, g_service=g_service, gsheet_tasks=gsheet_tasks, worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded, destination_gsheet_names=destination_gsheet_names, work_specs=work_specs, find_replace_patterns=find_replace_patterns, worksheet_defs=worksheet_defs)
            # work_on_gsheet(g_sheet=g_sheet, g_service=g_service, worksheet_names=worksheet_names, destination_gsheet_names=destination_gsheet_names, work_specs=work_specs, find_replace_patterns=find_replace_patterns)
            info(f"processed  {count:>4}/{num_gsheets} gsheet {gsheet_name}\n")

        if count % 100 == 0:
            warn(f"sleeping for {wait_for} seconds\n")
            time.sleep(wait_for)

