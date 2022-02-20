#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'code-sanity':      {'start-col': 'B', 'end-col': 'H', 'numerize': True}
}

class CodeSanityReader(GsheetReader):

    _label = 'code-sanity configuration data from gsheet'

    def read(self):

        data = None
        return data, self._log
