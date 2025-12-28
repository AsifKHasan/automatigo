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
    def __init__(self, service_account_json_path, config):

        # get credentials for service-account
        credentials = service_account.Credentials.from_service_account_file(service_account_json_path)
        scoped_credentials = credentials.with_scopes(SCOPES)

        # the gsheet service
        self.gsheet_service = build('sheets', 'v4', credentials=credentials)

        # the drive service
        self.drive_service = build('drive', 'v3', credentials=credentials)

        # using gspread for proxying the gsheet API's
        self.gspread = gspread.authorize(scoped_credentials)

        self.wait_for = config.get('wait-for', 60)
        self.try_for = config.get('try-for', 60)


    ''' open a gsheet
    '''
    def open_gsheet(self, gsheet_name, nesting_level=0):
        gspread_sheet = None
        for try_count in range(1, self.try_for+1):
            try:
                gspread_sheet = self.gspread.open(gsheet_name)
                break

            except Exception as e:
                print(e)
                if try_count < self.try_for:
                    warn(f"open gsheet failed in [{try_count}] try, trying again in {self.wait_for} seconds", nesting_level=1)
                    time.sleep(self.wait_for)
                else:
                    warn(f"open gsheet failed in [{try_count}] try", nesting_level=1)

        if gspread_sheet:
            return GoogleSheet(google_service=self, gspread_sheet=gspread_sheet, wait_for=self.wait_for, try_for=self.try_for)
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
            
            for try_count in range(1, self.try_for+1):
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
                    if try_count < self.try_for:
                        warn(f"An error occurred in [{try_count}] try: {err}, trying again in {self.wait_for} seconds", nesting_level=nesting_level)
                        time.sleep(self.wait_for)
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



    def share(self, file_id, email, perm_type, role, nesting_level=0):
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
    def get_drive_file(self, drive_file_name, folder_id=None, verbose=False, nesting_level=0):
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
                if verbose:
                    if len(files) > 1:
                        warn(f"multiple drive files found for [{drive_file_name}] ... ", nesting_level=nesting_level)

                    for i, drive_file in enumerate(files, start=1):
                        full_path = self.get_file_hierarchy(file_id=drive_file['id'])
                        path_name = " -> ".join([item['name'] for item in reversed(full_path)])
                        if i == 1:
                            trace(f"{i} : {path_name}", nesting_level=nesting_level)
                        else:
                            warn(f"{i} : {path_name}", nesting_level=nesting_level)


                return files[0]

        except Exception as error:
            print(f"An error occurred: {error}", nesting_level=nesting_level)
            return None



    '''
    Recursively retrieves the full parent folder hierarchy for a given file ID.

    Args:
        file_id (str): The ID of the file to trace.
        service: The authenticated Google Drive API service object.

    Returns:
        list: A list of dicts representing the path from the file up to the root.
              Example: [{'id': 'fileId', 'name': 'MyFile'}, {'id': 'parent1Id', 'name': 'Folder A'}, ...]
    '''
    def get_file_hierarchy(self, file_id, nesting_level=0):
        hierarchy = []
        current_id = file_id

        # Use a loop to trace back the parents
        while current_id:
            try:
                # 1. Fetch file/folder metadata
                # We specifically request the 'id', 'name', and 'parents' fields
                file_metadata = self.drive_service.files().get(
                    fileId=current_id, 
                    fields='id, name, parents'
                ).execute()
                
                file_name = file_metadata.get('name')
                parent_ids = file_metadata.get('parents')
                
                # 2. Add the current item to the hierarchy list
                hierarchy.append({'id': current_id, 'name': file_name})

                # 3. Determine the next parent ID for the next iteration
                if parent_ids:
                    # Drive can have multiple parents; we typically follow the first one
                    # for a single path, or you could adapt this to trace all paths.
                    current_id = parent_ids[0] 
                else:
                    # No more parents means we have reached the root (My Drive)
                    current_id = None

            except Exception as e:
                error(f"An error occurred while fetching ID {current_id}: {e}")
                break
        
        # The hierarchy is built from the file upward; return it in that order.
        return hierarchy



    def copy_file(self, source_file_id, target_folder_id, target_file_title, nesting_level=0):
        ''' copy a file
        '''

        copied_file = {'name': target_file_title, 'parents' : [target_folder_id]}
        try:
            response = self.drive_service.files().copy(fileId=source_file_id, fields='id', body=copied_file).execute()
            print(response)
            return response
        except Exception as error:
            print(error)
            return None



    def copy_drive_file(self, origin_file_id, copy_title, nesting_level=0):
        """
        Copy an existing file.

        Args:
            service: Drive API service instance.
            origin_file_id: ID of the origin file to copy.
            copy_title: Title of the copy.

        Returns:
            The copied file if successful, None otherwise.
        """
        copied_file = {'title': copy_title}
        try:
            return self.drive.files().copy(fileId=origin_file_id, body=copied_file).execute()
        except(errors.HttpError, error):
            error(f"An error occurred: {error}", nesting_level=nesting_level)
            return None



    def download_drive_file(self, param, destination, context, nesting_level=0):
        f = context['drive'].CreateFile(param)
        f.GetContentFile(destination)



    def read_drive_file(self, drive_url, nesting_level=0):
        url = drive_url.strip()

        id = url.replace('https://drive.google.com/file/d/', '')
        id = id.split('/')[0]
        # debug(f"drive file id to be read from is {id}", nesting_level=nesting_level)
        f = self.drive.CreateFile({'id': id})
        if f['mimeType'] != 'text/plain':
            warn(f"drive url {url} mime-type is {f['mimeType']} which may not be readable as text", nesting_level=nesting_level)

        text = f.GetContentString()
        return text

