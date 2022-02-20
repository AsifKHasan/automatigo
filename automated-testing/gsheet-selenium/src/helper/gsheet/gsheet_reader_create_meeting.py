#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan
from helper.gsheet.gsheet_reader import GsheetReader

WORKSHEETS = {
    'test-case':     {'start-col': 'B', 'end-col': 'G', 'numerize': True},
    'basic-info':    {'start-col': 'B', 'end-col': 'O', 'numerize': False},
    'background':    {'start-col': 'B', 'end-col': 'D', 'numerize': True},
    'agenda':        {'start-col': 'B', 'end-col': 'D', 'numerize': True},
    'key-personnel': {'start-col': 'B', 'end-col': 'G', 'numerize': True},
    'attachment':    {'start-col': 'B', 'end-col': 'D', 'numerize': True},
    'attendee':      {'start-col': 'B', 'end-col': 'P', 'numerize': True},
    'workflow':      {'start-col': 'A', 'end-col': 'H', 'numerize': True}
}

def list_of_dict(g):
    l = g.set_index('process').to_dict('records')
    l = [{k: v for k, v in d.items() if v is not None}  for d in l]
    l = [{k: v for k, v in d.items() if v is not None}  for d in l]

    return l

class CreateMeetingGsheetReader(GsheetReader):

    def df_from_worksheet(self, ws_title):
        self.info('reading worksheet: {0}'.format(ws_title))
        ws = self._context['gsheet'].worksheet('title', ws_title)
        if WORKSHEETS[ws_title]['numerize']:
            return ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=True, start='{0}2'.format(WORKSHEETS[ws_title]['start-col']), end='{0}{1}'.format(WORKSHEETS[ws_title]['end-col'], ws.rows))
        else:
            return ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=False, start='{0}2'.format(WORKSHEETS[ws_title]['start-col']), end='{0}{1}'.format(WORKSHEETS[ws_title]['end-col'], ws.rows))

    def merge_into_case(self, ws_title, data):
        for case, case_data in data.items():
            if case in self._cases:
                self._cases[case][ws_title] = case_data

    def read_gsheet(self, context):
        self._context = context

        # test-case
        df = self.df_from_worksheet('test-case')
        self._cases = df.set_index('case').T.to_dict('dict')

        # basic-info
        df = self.df_from_worksheet('basic-info')
        df = df[df['case'] != '']
        data = df.set_index('case').T.to_dict('dict')
        self.merge_into_case('basic-info', data)

        # background
        df = self.df_from_worksheet('background')
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case('background', data)

        # agenda
        df = self.df_from_worksheet('agenda')
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case('agenda', data)

        # key-personnel
        df = self.df_from_worksheet('key-personnel')
        data = df.set_index('case').T.to_dict('dict')
        self.merge_into_case('key-personnel', data)

        # attachment
        df = self.df_from_worksheet('attachment')
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case('attachment', data)

        # attendee
        df = self.df_from_worksheet('attendee')
        df = df[df['case'] != '']
        data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()
        self.merge_into_case('attendee', data)

        # workflow
        df = self.df_from_worksheet('workflow')
        # forward fill
        df.process = pd.Series(df.process).fillna(method='ffill')
        df.work = pd.Series(df.work).fillna(method='ffill')
        df = df[df['action'].notnull()]
        df = df[df['skip'] != 'Yes']
        df = df.where((pd.notnull(df)), None)
        workflow = df.groupby('work', sort=False).apply(lambda g: g.set_index('work').groupby('process', sort=False).apply(lambda g: list_of_dict(g)).to_dict()).to_dict()

        return {'test-case': self._cases, 'workflow': workflow}, self._log
