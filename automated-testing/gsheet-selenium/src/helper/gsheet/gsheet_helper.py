#!/usr/bin/env python
'''
'''

import pygsheets

import httplib2

from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient import discovery
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class GsheetHelper(object):

    def init(self, config):
        self._context = {}

        _G = pygsheets.authorize(service_account_file=config['files']['google-cred'])

        self._context['_G'] = _G
        sheet = _G.open(config['test']['data']['gsheet'])
        self._context['gsheet'] = sheet

        credentials = ServiceAccountCredentials.from_json_keyfile_name(config['files']['google-cred'], scopes=['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets'])
        credentials.authorize(httplib2.Http())

        self._context['service'] = discovery.build('sheets', 'v4', credentials=credentials)

        gauth = GoogleAuth()
        gauth.credentials = credentials

        self._context['drive'] = GoogleDrive(gauth)
        self._context['tmp-dir'] = config['dirs']['temp-dir']

        return self._context
