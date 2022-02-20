#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'database-schema':      {'start-col': 'B', 'end-col': 'H', 'numerize': True}
}

class DatabaseSchemaReader(GsheetReader):

    _label = 'database-schema configuration data from gsheet'

    def read(self):

        data = None
        return data, self._log
