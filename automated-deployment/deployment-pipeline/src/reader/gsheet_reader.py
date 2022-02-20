#!/usr/bin/env python3
'''
'''
from collections import defaultdict

import re
import importlib
import time
from datetime import datetime

import pygsheets
import pandas as pd

import urllib.request

from helper.logger import Logger
from helper.gsheet_util import *

class GsheetReader(Logger):

    def df_from_worksheet(self, ws_title, ws_data_spec):
        self._time_1 = time.time()
        self.debug('reading worksheet: {0}'.format(ws_title), console=True)
        ws = self._config['gsheet'].worksheet('title', ws_title)
        if ws_data_spec['numerize']:
            df = ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=True, start='{0}2'.format(ws_data_spec['start-col']), end='{0}{1}'.format(ws_data_spec['end-col'], ws.rows))
        else:
            df = ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=False, start='{0}2'.format(ws_data_spec['start-col']), end='{0}{1}'.format(ws_data_spec['end-col'], ws.rows))

        self.debug('worksheet read: {0}'.format(ws_title), time_1=self._time_1, console=True)

        return df

    def __init__(self, config, pipeline_data):
        self._config = config
        self._pipeline_data = pipeline_data
        self.start_time = time.time()
        self._enabled_repositories=None
        super().__init__()

    def __del__(self):
        self.info('{0} done'.format(self._label), time_0=self.start_time, console=True)
