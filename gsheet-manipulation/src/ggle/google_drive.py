#!/usr/bin/env python

from helper.utils import *
from helper.logger import *
from googleapiclient.errors import HttpError

''' Google sheet wrapper
'''
class GoogleDrive(object):

    ''' constructor
    '''
    def __init__(self, google_service, google_drive):
        self.service = google_service
        self.drive_service = google_drive


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

        except HttpError as error:
            print(f"An error occurred: {error}")
            return None



    ''' copy a file
    '''
    def copy_file(self, source_file_id, target_folder_id, target_file_title):
        copied_file = {'name': target_file_title, 'parents' : [target_folder_id]}
        try:
            response = self.drive_service.files().copy(fileId=source_file_id, fields='id', body=copied_file).execute()
            print(response)
            return response
        except Exception as error:
            print(error)
            return None


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
    def share(self, file_id, email, perm_type, role):
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


    def copy_drive_file(self, origin_file_id, copy_title, nesting_level):
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


    def download_drive_file(self, param, destination, context, nesting_level):
        f = context['drive'].CreateFile(param)
        f.GetContentFile(destination)


    def read_drive_file(self, drive_url, nesting_level):
        url = drive_url.strip()

        id = url.replace('https://drive.google.com/file/d/', '')
        id = id.split('/')[0]
        # debug(f"drive file id to be read from is {id}", nesting_level=nesting_level)
        f = self.drive.CreateFile({'id': id})
        if f['mimeType'] != 'text/plain':
            warn(f"drive url {url} mime-type is {f['mimeType']} which may not be readable as text", nesting_level=nesting_level)

        text = f.GetContentString()
        return text
