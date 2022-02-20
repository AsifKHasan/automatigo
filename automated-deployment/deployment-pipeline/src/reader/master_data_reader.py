#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'master-data':      {'start-col': 'B', 'end-col': 'H', 'numerize': True}
}

class MasterDataReader(GsheetReader):

    _label = 'master-data configuration data from gsheet'

    def read(self):

        data = None
        return data, self._log
