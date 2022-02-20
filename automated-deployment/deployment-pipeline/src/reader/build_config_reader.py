#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'build-config':      {'start-col': 'B', 'end-col': 'J', 'numerize': True}
}

class BuildConfigReader(GsheetReader):

    _label = 'build-config configuration data from gsheet'

    def read(self):
        ws_name='build-config'
        df = self.df_from_worksheet(ws_name, WORKSHEETS[ws_name])
        df = df[df['repo'].isin(self._pipeline_data['git-repo']['enabled_repositories'])]
        data = df.set_index('repo').T.to_dict('dict')
        
        return data, self._log
