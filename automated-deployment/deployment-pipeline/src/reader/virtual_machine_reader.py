#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'virtual-machine':      {'start-col': 'B', 'end-col': 'M', 'numerize': True}
}

class VirtualMachineReader(GsheetReader):

    _label = 'virtual-machine configuration data from gsheet'

    def read(self):

        df = self.df_from_worksheet('virtual-machine', WORKSHEETS['virtual-machine'])
        df['stakeholder'] = pd.Series(df['stakeholder']).fillna(method='ffill')

        # force missing values to None
        df = df.where((pd.notnull(df)), None)

        # remove rows where host-name is blank
        df = df[df['host-name'].notnull()]

        # remove rows where deploy flag is not set
        df = df[df['deploy'] == 'Yes']

        # nested dictionry stakeholder -> vm-type -> host-name
        data = df.groupby('stakeholder', sort=False)\
                    .apply(lambda g: g.groupby('vm-type', sort=False)\
                        .apply(lambda g: g[df.columns.difference(['stakeholder', 'vm-type'])].set_index('host-name').T.to_dict())\
                    .to_dict())\
                .to_dict()

        return data, self._log
