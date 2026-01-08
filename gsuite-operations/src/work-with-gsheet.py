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

''' execute gsheet tasks sequentially as defined in conf/data.yml *gsheet-tasks* list
    actual task parameters are defined in conf/task-defs.yml
'''
def execute_gsheet_tasks(g_sheet, g_service, gsheet_tasks=[], task_defs={}, worksheet_names=[], worksheet_names_excluded=[], nesting_level=0):
    for count, gsheet_task in enumerate(gsheet_tasks):
        if count:
            print()

        # get the task definition
        if gsheet_task not in task_defs:
            warn(f"task [{gsheet_task}] not defined in conf/task-def.yml", nesting_level=nesting_level)
            continue

        gsheet_task_def = task_defs.get(gsheet_task)
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
                        args_dict[k] = g_sheet.matching_worksheet_names(worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded, nesting_level=nesting_level+1)
                    else:
                        args_dict[k] = worksheet_names

                else:
                    args_dict[k] = v

            # matching_worksheet_names argument is not to be passed
            args_dict.pop('match_worksheet_names', None)


            # execute the task
            try:
                task = getattr(g_sheet, task_name)
                info(f"executing task [{task_name}]", nesting_level=nesting_level)

                if 'worksheet_names' in args_dict:
                    debug(f"worksheets to work on {args_dict['worksheet_names']}", nesting_level=nesting_level)
                    for x in args_dict['worksheet_names']:
                        trace(f"{x}", nesting_level=nesting_level)

                task(nesting_level=nesting_level+1, **args_dict)
                info(f"executed  task [{task_name}]", nesting_level=nesting_level)
            except Exception as e:
                error(str(e), nesting_level=nesting_level)

        else:
            error(f"g_sheet has no method [{task_name}]", nesting_level=nesting_level)


''' run some adhoc tasks not covered by tasks as defined in conf/data.yml *gsheet-tasks* list
'''
def work_on_gsheet(g_sheet, g_service, worksheet_names=[], worksheet_names_excluded=[], nesting_level=0):
    # -----------------------------------------------------------
    # BEGIN common tasks

    # new_toc_from_toc(g_sheet)

    # END   common tasks
    # -----------------------------------------------------------


    # -----------------------------------------------------------
    # BEGIN adhoc tasks

    # populate_range(g_sheet=g_sheet)
    # insert_a_row_with_values(g_sheet=g_sheet)

    # END   adhoc tasks
    # -----------------------------------------------------------


    # -----------------------------------------------------------
    # BEGIN resume specific tasks

    # web_image_to_drive_file_link_for_artifacts(g_sheet=g_sheet, g_service=g_service, worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded, nesting_level=nesting_level)

    # worksheet_names_to_work_on = ['02-career-highlight']
    # range_spec = 'B3:Z'
    # grouping_columns = 1
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=worksheet_names_to_work_on, range_spec=range_spec, grouping_columns=grouping_columns)

    # worksheet_names_to_work_on = ['04-managerial-expertise', '05-technical-expertise']
    # range_spec = 'B4:Z'
    # grouping_columns = 1
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=worksheet_names_to_work_on, range_spec=range_spec, grouping_columns=grouping_columns)

    # worksheet_names_to_work_on = ['06-job-history', '07-project-roles', '07-project-roles-RHD-TMC']
    # range_spec = 'B4:Z'
    # grouping_columns = 2
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=worksheet_names_to_work_on, range_spec=range_spec, grouping_columns=grouping_columns)

    # END   resume specific tasks
    # -----------------------------------------------------------


    # -----------------------------------------------------------
    # BEGIN PDS specific tasks

    # worksheet_names_to_work_on = ['06-description', '07-functionality', '08-technology', '09-services', '10-process']
    # range_spec = 'B3:Z'
    # grouping_columns = 1
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=worksheet_names_to_work_on, range_spec=range_spec, grouping_columns=grouping_columns)

    # worksheet_names_to_work_on = ['05-people']
    # range_spec = 'B3:Z'
    # grouping_columns = 2
    # border_and_merge_based_on_column(g_sheet=g_sheet, worksheet_names=worksheet_names_to_work_on, range_spec=range_spec, grouping_columns=grouping_columns)

    # END   PDS specific tasks
    # -----------------------------------------------------------


    # -----------------------------------------------------------
    # BEGIN drive/file related

    # g_sheet.share(email='asif.hasan@gmail.com', perm_type='user', role='owner')

    # END   drive/file related
    # -----------------------------------------------------------

    pass



if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-g", "--gsheet", required=False, help="gsheet name to work with", default=argparse.SUPPRESS)
    args = vars(ap.parse_args())

    # read config.yml to get the list of gsheets and other data
    config = yaml.load(open('../conf/data.yml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    logger.LOG_LEVEL = config.get('log-level', 0)

    # read task-defs.yml to get the task definitions
    task_defs = yaml.load(open('../conf/task-defs.yml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)


    # first we check whether the gsheet argument was passed or not
    if 'gsheet' in args and args["gsheet"] != '':
        gsheet_names = [args["gsheet"]]
    else:
        gsheet_names = config['gsheets']

    credential_json = config['credential-json']

    gsheet_tasks = config.get('gsheet-tasks', [])
    if gsheet_tasks is None: gsheet_tasks = []

    worksheet_names = config.get('worksheet-names', [])
    if worksheet_names is None: worksheet_names = []

    worksheet_names_excluded = config.get('worksheet-names-excluded', [])
    if worksheet_names_excluded is None: worksheet_names_excluded = []

    g_service = GoogleService(service_account_json_path=credential_json, config=config)

    wait_for = config.get('wait-for', 60)
    batch_size = config.get('batch-size', 100)
    num_gsheets = len(gsheet_names)
    nesting_level = 0
    for count, gsheet_name in enumerate(gsheet_names, start=1):
        try:
            if count:
                print()

            info(f"processing {count:>4}/{num_gsheets} gsheet {gsheet_name}", nesting_level=nesting_level)
            g_sheet = g_service.open_gsheet(gsheet_name=gsheet_name, nesting_level=nesting_level+1)
            
        except Exception as e:
            g_sheet = None
            warn(str(e), nesting_level=nesting_level)
            # raise e

        if g_sheet:
            execute_gsheet_tasks(g_sheet=g_sheet, g_service=g_service, gsheet_tasks=gsheet_tasks, task_defs=task_defs, worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded, nesting_level=nesting_level+1)
            # work_on_gsheet(g_sheet=g_sheet, g_service=g_service, worksheet_names=worksheet_names, worksheet_names_excluded=worksheet_names_excluded, nesting_level=nesting_level+1)
            info(f"processed  {count:>4}/{num_gsheets} gsheet {gsheet_name}", nesting_level=nesting_level)

        if count % batch_size == 0:
            warn(f"sleeping for {wait_for} seconds\n", nesting_level=nesting_level)
            time.sleep(wait_for)

