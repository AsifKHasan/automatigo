#!/usr/bin/env python
'''
'''

from googleapiclient import errors

def copy_file(service, origin_file_id, copy_title):
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
        return service.files().copy(fileId=origin_file_id, body=copied_file).execute()
    except(errors.HttpError, error):
        print('An error occurred: {0}'.format(error))
        return None

def download_file(param, destination, context):
    f = context['drive'].CreateFile(param)
    f.GetContentFile(destination)
