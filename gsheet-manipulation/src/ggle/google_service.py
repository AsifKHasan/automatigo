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

        # authed_session = AuthorizedSession(credentials)
        # response = authed_session.get('https://www.googleapis.com/storage/v1/b')

        # authed_http = AuthorizedHttp(credentials)
        # response = authed_http.request('GET', 'https://www.googleapis.com/storage/v1/b')


    ''' open a gsheet
    '''
    def open(self, gsheet_name, try_for=3):
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


    def list_files(self, parent_id, path_prefix=""):
        ''' Recursively lists all files and folders under a given parent ID

            Args:
                parent_id: The ID of the current folder to search within.
            Returns:
                list of file metadata, or None
        '''

        page_token = None
        
        all_items = []
        while True:
            # Search query: List items where the parent is the current ID and not trashed.
            # We also need to query for the MIME type to distinguish files from folders.
            query = f"'{parent_id}' in parents and trashed = false"
            
            results = self.drive_service.files().list(
                q=query,
                fields="nextPageToken, files(id, name, mimeType, owners)",
                pageSize=1000, 
                pageToken=page_token
            ).execute()
            
            items = results.get('files', [])

            all_items = all_items + items

            for item in items:
                name = item['name']
                file_id = item['id']
                mime_type = item['mimeType']
                full_path = f"{path_prefix}/{name}"

                # Check if the item is a folder
                if mime_type == 'application/vnd.google-apps.folder':
                    print(f"📁 Found Folder: {full_path}")
                    # RECURSIVE CALL: Call the function again for the subfolder
                    all_items = all_items + self.list_files(file_id, full_path)


            page_token = results.get('nextPageToken')
            if not page_token:
                break


        return all_items



    def list_files_under(self, folder_id):
        """Main function to start the search"""
        try:
            # Get the name of the starting folder for the path_prefix
            start_folder = self.drive_service.files().get(
                fileId=folder_id, 
                fields='name'
            ).execute()
            start_name = start_folder.get('name', 'Root Folder')
            
            folder_items = self.list_files(folder_id, start_name)

            all_items = []
            for i, item in enumerate(folder_items, start=1):
                # The 'owners' field is an array of users who own the file (usually just one)
                owners = item.get('owners', [])
                
                owner_email = "N/A"
                if owners:
                    # Get the emailAddress from the first owner in the list
                    owner_email = owners[0].get('emailAddress', 'Unknown Owner')

                all_items.append({'file_name': item['name'], 'id': item['id'], 'mime_type': item['mimeType'], 'owner': owner_email})

            return all_items
            
        except Exception as error:
            print(f'An error occurred: {error}')



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



