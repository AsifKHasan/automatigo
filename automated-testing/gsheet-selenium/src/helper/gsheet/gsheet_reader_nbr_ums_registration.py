#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan
from helper.gsheet.gsheet_reader import GsheetReader
from helper.logger import *

WS_LIST = {
    'login':    {'start-col': 'B', 'end-col': 'D', 'numerize': True},
}

class NbrUmsRegistrationGsheetReader(GsheetReader):

    def read_gsheet(self, context):
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

        return {'test-case': self._cases, 'workflow': workflow}, self._log
