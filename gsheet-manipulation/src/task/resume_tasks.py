#!/usr/bin/env python3

import gspread
from gspread.utils import *
from gspread.exceptions import *
from gspread_formatting import *

from pprint import pprint

from helper.utils import *
from helper.logger import *


''' merge cells and border worksheet based on one column
'''
def border_and_merge_based_on_column(g_sheet, worksheet_names, range_spec, grouping_columns):
    values, requests = [], []
    for worksheet_name in worksheet_names:
        range_work_specs = {}
        worksheet = g_sheet.worksheet_by_name(worksheet_name=worksheet_name)
        if worksheet is None:
            error(f"worksheet {worksheet_name} not found", nesting_level=1)
            continue

        # unmerge the range
        grid_range = a1_range_to_grid_range(range_spec, sheet_id=worksheet.id)
        # requests.append({'unmergeCells': {'range': grid_range}})
        vals, reqs = worksheet.range_work_requests(range_work_specs={range_spec: {'border-color': '#B7B7B7', 'no-border': True, }})
        requests = requests + reqs
        values = values + vals


        # first column of range B (1) is the grouping column, vertical span for each value is to be stored (for subsequent column processing), merged and bordered around
        grouping_start_column = grid_range['startColumnIndex'] + 1
        grouping_end_column = grouping_start_column + grouping_columns - 1
        non_grouping_start_column = grouping_end_column + 1
        last_column = grid_range['endColumnIndex']
        start_row = grid_range['startRowIndex']

        range_values = worksheet.get_values_in_batch(ranges=[range_spec])
        group_start_row = 0
        current_row = 0
        for row in range_values[0]:
            if len(row) != 0:
                new_value = row[0]
                if current_row == 0:
                    previous_value = row[0]
                else:
                    if new_value != '' and new_value != previous_value:
                        # print(f"[{COLUMN_TO_LETTER[grouping_column]}{start_row+current_row+1}] value changed [{previous_value}] -> [{new_value}]")
                        a1_range = f"{COLUMN_TO_LETTER[grouping_start_column]}{start_row+group_start_row+1}:{COLUMN_TO_LETTER[grouping_end_column]}{start_row+current_row}"
                        range_work_specs[a1_range] = {'merge': True, 'border-color': '#B7B7B7', 'merge-type': 'MERGE_COLUMNS', }
                        a1_range = f"{COLUMN_TO_LETTER[non_grouping_start_column]}{start_row+group_start_row+1}:{COLUMN_TO_LETTER[last_column]}{start_row+current_row}"
                        range_work_specs[a1_range] = {'border-color': '#B7B7B7', 'inner-border': False, }

                        group_start_row = current_row
                        previous_value = new_value

            current_row = current_row + 1

        # there may be an open group
        if group_start_row < current_row:
            a1_range = f"{COLUMN_TO_LETTER[grouping_start_column]}{start_row+group_start_row+1}:{COLUMN_TO_LETTER[grouping_end_column]}{start_row+current_row}"
            range_work_specs[a1_range] = {'merge': True, 'border-color': '#B7B7B7', 'merge-type': 'MERGE_COLUMNS', }
            # do for the other columns
            a1_range = f"{COLUMN_TO_LETTER[non_grouping_start_column]}{start_row+group_start_row+1}:{COLUMN_TO_LETTER[last_column]}{start_row+current_row}"
            range_work_specs[a1_range] = {'border-color': '#B7B7B7', 'inner-border': False, }

        vals, reqs = worksheet.range_work_requests(range_work_specs=range_work_specs)
        requests = requests + reqs
        values = values + vals

        # pprint(range_work_specs)

    g_sheet.update_in_batch(values=values, requests=requests, requester='border_and_merge_based_on_column')



''' modify 06-job-history to new format
'''
def create_06_job_history_new(gsheet):
    # get job-histories data from 06-job-history
    job_history_ws_name = '06-job-history'
    job_history_ws = gsheet.gspread_sheet.worksheet(job_history_ws_name)
    if job_history_ws is None:
        error(f"worksheet {job_history_ws_name} not found", nesting_level=1)
        return

    WORKSHEET_SPEC = WORKSHEET_SPECS['06-job-history']

    # get the job-history list
    job_histories = job_history_from_06_job_history(job_history_ws)

    # duplicate the *06-job-history* as *06-job-history-NEW* worksheet
    target_ws_name = '06-job-history-NEW'
    info(f"duplicating .. worksheet {job_history_ws_name} as {target_ws_name}", nesting_level=1)
    target_ws = job_history_ws.duplicate(new_sheet_name=target_ws_name)
    if target_ws:
        info(f"duplicated  .. worksheet {job_history_ws_name} as {target_ws_name}", nesting_level=1)
    else:
        error(f"could not duplicate   {job_history_ws_name} as {target_ws_name}", nesting_level=1)
        return

    col_count = target_ws.col_count
    row_count = target_ws.row_count


    # add 4 new columns at the end (after D) E, F, G, H and add job_histories.count * 3 + rows at the end
    # HACK - for safety add 1000 rows at the end
    cols_to_add_at, cols_to_add, rows_to_add_at, rows_to_add = 'B', 4, 'end', 1000
    info(f"adding .. {cols_to_add} new columns at {cols_to_add_at} and {rows_to_add} new rows at {rows_to_add_at}", nesting_level=1)
    gsheet.add_dimension(worksheet_id=target_ws.id, cols_to_add_at=cols_to_add_at, cols_to_add=cols_to_add, rows_to_add_at=rows_to_add_at, rows_to_add=rows_to_add)
    info(f"added  .. {cols_to_add} new columns at {cols_to_add_at} and {rows_to_add} new rows at {rows_to_add_at}", nesting_level=1)

    col_count = col_count + 4
    row_count = row_count + 1000


    # add 4 new columns at the end (after D) E, F, G, H
    # info(f"adding .. 4 new columns at E-H", nesting_level=1)
    # target_ws.insert_cols([[], [], [], []], 2)
    # col_count = col_count + 4
    # info(f"added  .. 4 new columns at E-H", nesting_level=1)


    # add job_histories.count * 3 + rows at the end
    # HACK - for safety add 1000 rows at the end
    # target_ws.add_rows(job_histories.length * 3 + 1)
    # info(f"adding .. 1000 new rows at the end", nesting_level=1)
    # target_ws.add_rows(1000)
    # row_count = row_count + 1000
    # info(f"added  .. 1000 new rows at the end", nesting_level=1)


    info(f"resizing .. columns", nesting_level=1)
    target_ws.resize_columns(WORKSHEET_SPEC['columns'])
    info(f"resized  .. columns", nesting_level=1)


    # iterate job-histories and create range_work_specs
    range_work_specs = {}
    current_row = 4
    index = 0
    info(f"generating .. dynamic ranges", nesting_level=1)
    for job_history in job_histories:
        block_start_row = current_row

        range_spec = ''

        # Organization - label
        range_spec = f"D{current_row}:E{current_row}"
        range_work_specs[range_spec] = {'value': 'Organization', 'halign': 'left', 'bgcolor': '#f3f3f3', 'weight': 'bold'}

        current_row = current_row + 1

        for s in job_history['name']:
            range_spec = f"D{current_row}:E{current_row}"
            range_work_specs[range_spec] = {'value': s, 'halign': 'left', 'weight': 'normal'}
            current_row = current_row + 1

        # Position - label
        range_spec = f"D{current_row}:E{current_row}"
        range_work_specs[range_spec] = {'value': 'Position', 'halign': 'left', 'bgcolor': '#f3f3f3', 'weight': 'bold'}

        current_row = current_row + 1

        for s in job_history['position']:
            range_spec = f"D{current_row}:E{current_row}"
            range_work_specs[range_spec] = {'value': s, 'halign': 'left', 'weight': 'normal'}
            current_row = current_row + 1

        # Job Summary - label
        range_spec = f"D{current_row}:E{current_row}"
        range_work_specs[range_spec] = {'value': 'Job Summary', 'halign': 'left', 'bgcolor': '#f3f3f3', 'weight': 'bold'}

        current_row = current_row + 1

        for s in job_history['summary']:
            range_spec = f"D{current_row}"
            range_work_specs[range_spec] = {'value': '•', 'halign': 'center'}
            range_spec = f"E{current_row}"
            range_work_specs[range_spec] = {'value': s, 'halign': 'left', 'weight': 'normal'}
            current_row = current_row + 1


        # job-history finished
        block_end_row = current_row - 1

        # From
        range_spec = f"B{block_start_row}:B{block_end_row}"
        # val = quote_number(job_history['from'])
        val = job_history['from']
        # debug(f".. From : {job_history['from']} -> {val}")
        range_work_specs[range_spec] = {'value': val, 'border-color': '#b7b7b7'}

        # To
        range_spec = f"C{block_start_row}:C{block_end_row}"
        # val = quote_number(job_history['to'])
        val = job_history['to']
        # debug(f".. To   : {job_history['to']} -> {val}")
        range_work_specs[range_spec] = {'value': val, 'border-color': '#b7b7b7'}

        # border around column D and E
        range_spec = f"D{block_start_row}:E{block_end_row}"
        range_work_specs[range_spec] = {'border-color': '#b7b7b7', 'merge': False}

        index = index + 1


    info(f"generated  .. {index} dynamic ranges", nesting_level=1)

    # iterate over ranges and apply specs
    info(f"formatting .. ranges", nesting_level=1)
    count = gsheet.work_on_ranges(worksheet=target_ws, range_work_specs={**WORKSHEET_SPEC['ranges'], **range_work_specs})
    info(f"formatted  .. {count} ranges", nesting_level=1)


    # remove last 3 columns and trailing blank rows
    cols_to_remove_from, cols_to_remove_to = 'F', 'end'
    rows_to_remove_from, rows_to_remove_to = gsheet.trailing_blank_row_start_index(worksheet=target_ws), 'end'
    info(f"removing .. columns {cols_to_remove_from}-{cols_to_remove_to} and rows {rows_to_remove_from}-{rows_to_remove_to}", nesting_level=1)
    gsheet.remove_dimension(worksheet_id=target_ws.id, cols_to_remove_from=cols_to_remove_from, cols_to_remove_to=cols_to_remove_to, rows_to_remove_from=rows_to_remove_from, rows_to_remove_to=rows_to_remove_to)
    info(f"removed  .. columns {cols_to_remove_from}-{cols_to_remove_to} and rows {rows_to_remove_from}-{rows_to_remove_to}", nesting_level=1)


    # # remove last 3 columns
    # info(f"removing .. last 3 columns", nesting_level=1)
    # target_ws.delete_columns(6, 8)
    # col_count = col_count - 3
    # info(f"removed  .. last 3 columns", nesting_level=1)

    # # remove all trailing blank rows
    # info(f"removing .. trailing blank rows", nesting_level=1)
    # gsheet.remove_trailing_blank_rows(target_ws, row_count)
    # info(f"removed  .. trailing blank rows", nesting_level=1)


    # clear conditional formatting
    info(f"clearing .. all conditional formatting", nesting_level=1)
    gsheet.clear_conditional_format_rules(target_ws)
    info(f"cleared  .. all conditional formatting", nesting_level=1)


    # conditional formatting for blank cells
    info(f"adding .. conditional formatting for blank cells", nesting_level=1)
    gsheet.add_conditional_formatting_for_blank_cells(target_ws, WORKSHEET_SPEC['cell-empty-markers'])
    info(f"added  .. conditional formatting for blank cells", nesting_level=1)


    # conditional formatting review-notes
    info(f"adding .. conditional formatting for review-notes", nesting_level=1)
    gsheet.add_conditional_formatting_for_review_notes(target_ws, row_count, col_count)
    info(f"added  .. conditional formatting for review-notes", nesting_level=1)


    info(f"freezing .. {WORKSHEET_SPEC['frozen-rows']} rows and {WORKSHEET_SPEC['frozen-columns']} columns", nesting_level=1)
    try:
        target_ws.freeze(WORKSHEET_SPEC['frozen-rows'], WORKSHEET_SPEC['frozen-columns'])
        info(f"freezed  .. {WORKSHEET_SPEC['frozen-rows']} rows and {WORKSHEET_SPEC['frozen-columns']} columns", nesting_level=1)
    except Exception as e:
        warn(str(e))



''' get job-histories data from '06-job-history'
'''
def job_history_from_06_job_history(job_history_ws):
    LABEL_TO_GROUP = {
        'Organization': 'name',
        'Position': 'position',
        'Job Summary': 'summary',
    }

    GROUP_SUBGROUP = {
    }

    GROUP_VALUE_INDEX = {
        'name': 1,
        'position': 1,
        'summary': 2,
    }

    source_values = job_history_ws.get('B3:D')

    num_rows = len(source_values)
    current_row_index = 0
    job_histories = []
    new_job_history_found = False
    job_history = {}

    # loop until we have eaten up all rows
    while num_rows > current_row_index:
        current_row = source_values[current_row_index]
        # pprint(f"{current_row_index} : {current_row}")

        if len(current_row) > 0 and current_row[0] == 'Organization':
            # we have found the start of a new job-history

            # there may be a running job-history
            if len(job_history.keys()) != 0:
                job_history['end-row'] = current_row_index - 1
                job_histories.append(job_history)
                job_history = {}

            job_history['start-row'] = current_row_index

        current_row_index = current_row_index + 1

    # there may be a pending job-history
    if len(job_history.keys()) != 0:
        job_history['end-row'] = current_row_index - 1
        job_histories.append(job_history)

    # now we have a list of job-histories
    job_history_index = 0
    for job_history in job_histories:
        job_history['name'] = []
        job_history['position'] = []
        job_history['from'] = ''
        job_history['to'] = ''
        job_history['summary'] = []
        current_group = 'name'
        for i in range(job_history['start-row'], job_history['end-row'] + 1):
            row = source_values[i]

            # the row may be empty
            if len(row) == 0:
                continue

            # the group is the first value
            new_group_label = row[0]
            new_group_label = new_group_label.strip()

            if new_group_label == '':
                # previous group continuing
                group_value_index = GROUP_VALUE_INDEX[current_group]
                if len(row) > group_value_index:
                    value = row[GROUP_VALUE_INDEX[current_group]]

                    # group may have subgroups
                    if current_group in GROUP_SUBGROUP:
                        if value in GROUP_SUBGROUP[current_group]:
                            # the value is not value for the group rather it starts a subgroup
                            current_group = GROUP_SUBGROUP[current_group][value]

                        else:
                            # this is not a subgroup, append value
                            if value != '':
                                job_history[current_group] = job_history[current_group] + split_and_dress(value)

                    else:
                        # the group does not have any subgroups, append value
                        if value != '':
                            job_history[current_group] = job_history[current_group] + split_and_dress(value)

            else:
                # a new group has started, get the group
                if new_group_label in LABEL_TO_GROUP:
                    current_group = LABEL_TO_GROUP[new_group_label]

                    # append value into the group
                    group_value_index = GROUP_VALUE_INDEX[current_group]
                    if len(row) > group_value_index:
                        value = row[group_value_index]
                        if value != '':
                            job_history[current_group] = job_history[current_group] + split_and_dress(value)

                else:
                    # this must be the from value
                    job_history['from'] = new_group_label
                    if len(row) >= 3:
                        job_history['to'] = row[2]
                    else:
                        job_history['to'] = ''


        # we should have at least one entry for each groups
        if len(job_history['name']) == 0:
            job_history['name'].append('')

        if len(job_history['position']) == 0:
            job_history['position'].append('')

        if len(job_history['summary']) == 0:
            job_history['summary'].append('')

        if True:
            debug(f"project {job_history_index}", nesting_level=2)
            debug(f".. from     : {job_history['from']}", nesting_level=2)
            debug(f".. to       : {job_history['to']}", nesting_level=2)

            debug(f".. name     : {job_history['name'][0]}", nesting_level=2)
            for name in job_history['name'][1:]:
                debug(f"..          : {name}", nesting_level=2)

            debug(f".. position : {job_history['position'][0]}", nesting_level=2)
            for position in job_history['position'][1:]:
                debug(f"..          : {position}", nesting_level=2)

            debug(f".. summary  : {job_history['summary'][0]}", nesting_level=2)
            for summary in job_history['summary'][1:]:
                debug(f"..          : {summary}", nesting_level=2)

        job_history_index = job_history_index + 1


    return job_histories
