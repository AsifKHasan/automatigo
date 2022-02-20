#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'unit-test':      {'start-col': 'B', 'end-col': 'E', 'numerize': True}
}

class UnitTestReader(GsheetReader):

    _label = 'unit-test configuration data from gsheet'

    def read(self):
        ws_name='unit-test'
        df = self.df_from_worksheet(ws_name, WORKSHEETS[ws_name])
        df = df[df['repo'].isin(self._pipeline_data['git-repo']['enabled_repositories'])]
        data = df.set_index('repo').T.to_dict('dict')

        return data, self._log
