#!/usr/bin/env python

import gspread

from googleapiclient.discovery import build
from google.oauth2 import service_account
from apiclient import errors
from googleapiclient.errors import HttpError

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

