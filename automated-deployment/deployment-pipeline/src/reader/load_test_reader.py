#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'load-test':      {'start-col': 'B', 'end-col': 'H', 'numerize': True}
}

class LoadTestReader(GsheetReader):

    _label = 'load-test configuration data from gsheet'

    def read(self):

        data = None
        return data, self._log
