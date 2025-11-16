#!/usr/bin/env python

import gspread

from googleapiclient.discovery import build
from google.oauth2 import service_account
from apiclient import errors

from ggle.google_sheet import GoogleSheet

from helper.logger import *

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]


''' Google service wrapper
'''
class GoogleService(object):

    ''' constructor
    '''
    def __init__(self, service_account_json_path):

        # get credentials for service-account
        credentials = service_account.Credentials.from_service_account_file(service_account_json_path)
        scoped_credentials = credentials.with_scopes(SCOPES)

        # the gsheet service
        self.gsheet_service = build('sheets', 'v4', credentials=credentials)

        # the drive service
        self.drive_service = build('drive', 'v3', credentials=credentials)

        # using gspread for proxying the gsheet API's
        self.gspread = gspread.authorize(scoped_credentials)



    ''' open a gsheet
    '''
    def open_gsheet(self, gsheet_name, try_for=3):
        gspread_sheet = None
        wait_for = 30
        for try_count in range(1, try_for+1):
            try:
                gspread_sheet = self.gspread.open(gsheet_name)
                break

            except Exception as e:
                print(e)
                if try_count < try_for:
                    warn(f"open gsheet failed in [{try_count}] try, trying again in {wait_for} seconds", nesting_level=1)
                    time.sleep(wait_for)
                else:
                    warn(f"open gsheet failed in [{try_count}] try", nesting_level=1)

        if gspread_sheet:
            return GoogleSheet(google_service=self, gspread_sheet=gspread_sheet)
        else:
            return None


    ''' Recursively lists all files and folders under a given parent folder

        Args:
            parent_id: The ID of the current folder to search within
            path_prefix: path prefix of the folder to list files under
            recursive: whether ro recurse into sub-folders or not
        Returns:
            list of file metadata (as dict), or None
    '''
    def list_files(self, parent_id, path_prefix='', recursive=True, nesting_level=0):
        page_token = None
        
        all_items = []
        while True:
            # Search query: List items where the parent is the current ID and not trashed.
            # We also need to query for the MIME type to distinguish files from folders.
            query = f"'{parent_id}' in parents and trashed = false"
            
            wait_for = 30
            try_for = 3
            for try_count in range(1, try_for+1):
                try:
                    results = self.drive_service.files().list(
                        q=query,
                        fields="nextPageToken, files(id, name, webViewLink, mimeType, owners, size, quotaBytesUsed)",
                        pageSize=1000, 
                        pageToken=page_token
                    ).execute()

                    items = results.get('files', [])
                    trace(f"{len(items)} file(s) found", nesting_level=nesting_level+1)
                    break
                
                except Exception as err:
                    if try_count < try_for:
                        warn(f"An error occurred in [{try_count}] try: {err}, trying again in {wait_for} seconds", nesting_level=nesting_level)
                        time.sleep(wait_for)
                        continue

                    else:
                        error(f"An error occurred in [{try_count}] try: {err} .. abandoing", nesting_level=nesting_level)
                        items = []
                        break

            items = [dict(item, path=path_prefix) for item in items]
            all_items = all_items + items

            for item in items:
                file_id = item['id']
                name = item['name']
                mime_type = item['mimeType']
                full_path = f"{path_prefix}/{name}"

                # Check if the item is a folder
                if mime_type == 'application/vnd.google-apps.folder':
                    debug(f"📁 Found Folder: {full_path:<100} id=[{file_id}]", nesting_level=nesting_level)
                    if recursive:
                        # RECURSIVE CALL: Call the function again for the subfolder
                        this_list = self.list_files(file_id, full_path, nesting_level=nesting_level+1)
                        all_items = all_items + this_list

            page_token = results.get('nextPageToken')
            if not page_token:
                break

        return all_items



    ''' lists all files and folders under a given parent folder
    '''
    def list_files_under(self, folder_id, recursive=True, nesting_level=0):
        try:
            # Get the name of the starting folder for the path_prefix
            start_folder = self.drive_service.files().get(
                fileId=folder_id, 
                fields='name'
            ).execute()
            start_name = start_folder.get('name', 'Root Folder')
            
            folder_items = self.list_files(folder_id, start_name, recursive=recursive, nesting_level=nesting_level+1)
            # folder_items = [dict(item, path=start_name) for item in folder_items]

            all_items = []
            for i, item in enumerate(folder_items, start=1):
                # The 'owners' field is an array of users who own the file (usually just one)
                owners = item.get('owners', [])
                
                owner_email = "N/A"
                if owners:
                    # Get the emailAddress from the first owner in the list
                    owner_email = owners[0].get('emailAddress', 'Unknown Owner')

                all_items.append({'path': item['path'], 'file_name': item['name'], 'id': item['id'], 'view_link': item['webViewLink'], 'mime_type': item['mimeType'], 'owner': owner_email, 'bytes': item.get('size', 0), 'quota_bytes': item.get('quotaBytesUsed', 0)})

            return all_items
            
        except Exception as err:
            error(f'An error occurred: {err}')
            return None



    def share(self, file_id, email, perm_type, role):
        ''' share a file
            Args:
                service: Drive API service instance.
                file_id: ID of the file to insert permission for.
                value: User or group e-mail address, domain name or None for 'default'
                        type.
                perm_type: The value 'user', 'group', 'domain' or 'default'.
                role: The value 'owner', 'writer' or 'reader'.
            Returns:
                The inserted permission if successful, None otherwise.
        '''

        new_permission = {
            'emailAddress': email,
            'type': perm_type,
            'role': role
        }
        try:
            return self.drive_service.permissions().create(fileId=file_id, moveToNewOwnersRoot=True, transferOwnership=True, body=new_permission).execute()

        except Exception as error:
            print(error)

        return None



    ''' get a drive file
    '''
    def get_drive_file(self, drive_file_name, folder_id=None):
        if folder_id is not None:
            q = f"'{folder_id}' in parents and name = '{drive_file_name}'"
        else:
            q = f"name = '{drive_file_name}'"

        # print(q)

        try:
            files = []
            page_token = None
            while True:
                response = self.drive_service.files().list(q=q,
                                                spaces='drive',
                                                fields='nextPageToken, files(id, name, webViewLink)',
                                                pageToken=page_token).execute()

                files.extend(response.get('files', []))
                page_token = response.get('nextPageToken', None)
                if page_token is None:
                    break

            if len(files) > 0:
                return files[0]

        except Exception as error:
            print(f"An error occurred: {error}")
            return None




