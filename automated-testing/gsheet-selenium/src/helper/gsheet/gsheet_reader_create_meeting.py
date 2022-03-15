#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan
from helper.gsheet.gsheet_reader import GsheetReader
from helper.logger import *

WS_LIST = {
    'basic-info':    {'start-col': 'B', 'end-col': 'O', 'numerize': False},
    'background':    {'start-col': 'B', 'end-col': 'D', 'numerize': True},
    'agenda':        {'start-col': 'B', 'end-col': 'D', 'numerize': True},
    'key-personnel': {'start-col': 'B', 'end-col': 'G', 'numerize': True},
    'attachment':    {'start-col': 'B', 'end-col': 'D', 'numerize': True},
    'attendee':      {'start-col': 'B', 'end-col': 'P', 'numerize': True},
}

class CreateMeetingGsheetReader(GsheetReader):

    def read_gsheet(self):
        self.WORKSHEETS = z = {**self.WORKSHEETS, **WS_LIST}

        # workflow
        ws_name = 'workflow'
        df = self.df_from_worksheet(ws_name)
        # forward fill
        df.process = pd.Series(df.process).fillna(method='ffill')
        df.work = pd.Series(df.work).fillna(method='ffill')
        df = df[df['action'].notnull()]
        df = df[df['skip'] != 'Yes']
        df = df.where((pd.notnull(df)), None)
        workflow = df.groupby('work', sort=False).apply(lambda g: g.set_index('work').groupby('process', sort=False).apply(lambda g: list_of_dict(g)).to_dict()).to_dict()

        # test-case
        ws_name = 'test-case'
        df = self.df_from_worksheet(ws_name)
        self._cases = df.set_index('case').T.to_dict('dict')

        # basic-info
        ws_name = 'basic-info'
        df = self.df_from_worksheet(ws_name)
        df = df[df['case'] != '']
        data = df.set_index('case').T.to_dict('dict')
        self.merge_into_case(ws_name, data)

        # background
        ws_name = 'background'
        df = self.df_from_worksheet(ws_name)
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case(ws_name, data)

        # agenda
        ws_name = 'agenda'
        df = self.df_from_worksheet(ws_name)
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case(ws_name, data)

        # key-personnel
        ws_name = 'key-personnel'
        df = self.df_from_worksheet(ws_name)
        data = df.set_index('case').T.to_dict('dict')
        self.merge_into_case(ws_name, data)

        # attachment
        ws_name = 'attachment'
        df = self.df_from_worksheet(ws_name)
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case(ws_name, data)

        # attendee
        ws_name = 'attendee'
        df = self.df_from_worksheet(ws_name)
        df = df[df['case'] != '']
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case(ws_name, data)

        return {'test-case': self._cases, 'workflow': workflow}, self._log
