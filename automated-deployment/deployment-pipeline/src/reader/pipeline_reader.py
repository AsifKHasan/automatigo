#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from helper.gsheet_util import *
from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'pipeline':      {'start-col': 'B', 'end-col': 'H', 'numerize': True}
}

class PipelineReader(GsheetReader):

    _label = 'pipeline configuration data from gsheet'

    def init(self, gsheet_name, credential_json_path):
        # authorize
        self._config['google-authorization'] = authorize(credential_json_path)

        # open gsheet
        self._config['gsheet'] = self._config['google-authorization']['_G'].open(gsheet_name)

    def read(self):

        ws_name = 'pipeline'
        df = self.df_from_worksheet(ws_name, WORKSHEETS[ws_name])
        df = df.where((pd.notnull(df)), None)
        self._pipeline = df.set_index('stage').T.to_dict('dict')

        return self._pipeline, self._log
