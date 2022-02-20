#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'seed-data':      {'start-col': 'B', 'end-col': 'H', 'numerize': True}
}

class SeedDataReader(GsheetReader):

    _label = 'seed-data configuration data from gsheet'

    def read(self):

        data = None
        return data, self._log
