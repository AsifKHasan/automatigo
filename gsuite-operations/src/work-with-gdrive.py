#!/usr/bin/env python

import json
import yaml
import time
import argparse

from ggle.google_service import GoogleService

from helper.logger import *
from helper import logger
from helper.utils import *

final_list = []

def work_on_drive(g_service, folder_id):
    # target_file_id = g_service.copy_file(source_file_id=g_sheet.id(), target_folder_id='1Ol7pNkAloXNPxeU8j1_IMNAayUh7AvPf', target_file_title='BNDA__standards')
    # g_service.share(file_id=target_file_id, email='asif.hasan@gmail.com', perm_type='user', role='owner')
    # g_service.share(file_id='1J7VpUFfZiQi543f4zdGcX9mqX7HugvsmebtoECCgk_4', email='asif.hasan@gmail.com', perm_type='user', role='owner')
    files = g_service.list_files_under(folder_id=folder_id, recursive=False)
    files = [file for file in files if file['owner'] not in ['asif.hasan@gmail.com']]
    for i, file in enumerate(files, start=1):
        print(f"{i:<4} {file['file_name']:<100} {file['id']:<50} {file['mime_type']:<50} {file['owner']:<50}")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--folder", required=False, help="work with drive folder", action='store_true')
    args = vars(ap.parse_args())

    # read config.yml to get the list of gsheets and other data
    config = yaml.load(open('../conf/data.yml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    logger.LOG_LEVEL = config.get('log-level', 0)

    credential_json = config['credential-json']

    drive_folders = config.get('drive-folders', [])
    if drive_folders is None: drive_folders = []

    g_service = GoogleService(credential_json)

    wait_for = 30
    num_folders = len(drive_folders)
    for count, folder_id in enumerate(drive_folders, start=1):
        info(f"processing {count:>4}/{num_folders} folder {folder_id}")
        work_on_drive(g_service=g_service, folder_id=folder_id)
        info(f"processed  {count:>4}/{num_folders} folder {folder_id}\n")

        if count % 100 == 0:
            warn(f"sleeping for {wait_for} seconds\n")
            time.sleep(wait_for)


