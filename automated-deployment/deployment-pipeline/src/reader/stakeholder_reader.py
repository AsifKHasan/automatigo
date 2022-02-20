#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'stakeholder':      {'start-col': 'B', 'end-col': 'E', 'numerize': True}
}

class StakeholderReader(GsheetReader):

    _label = 'stakeholder configuration data from gsheet'

    def read(self):

        df = self.df_from_worksheet('stakeholder', WORKSHEETS['stakeholder'])
        df['stakeholder'] = pd.Series(df['stakeholder']).fillna(method='ffill')
        df = df.where((pd.notnull(df)), None)
        df = df[df['deploy'] == 'Yes']
        data = df.set_index('stakeholder').T.to_dict('dict')

        return data, self._log
