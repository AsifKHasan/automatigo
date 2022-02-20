#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'docker-container':      {'start-col': 'B', 'end-col': 'J', 'numerize': True}
}

class DockerContainerReader(GsheetReader):

    _label = 'docker-container configuration data from gsheet'

    def read(self):

        df = self.df_from_worksheet('docker-container', WORKSHEETS['docker-container'])
        df['stakeholder'] = pd.Series(df['stakeholder']).fillna(method='ffill')

        # force missing values to None
        df = df.where((pd.notnull(df)), None)

        # remove rows where host-vm or container-name is blank
        df = df[df['host-vm'].notnull()]
        df = df[df['container-name'].notnull()]

        # remove rows where deploy flag is not set
        # df = df[df['deploy'] == 'Yes']

        # nested dictionry stakeholder -> 'host-vm -> container-name
        data = df.groupby('stakeholder', sort=False)\
                    .apply(lambda g: g.groupby('host-vm', sort=False)\
                        .apply(lambda g: g[df.columns.difference(['stakeholder', 'host-vm'])].set_index('container-name').T.to_dict())\
                    .to_dict())\
                .to_dict()

        return data, self._log
