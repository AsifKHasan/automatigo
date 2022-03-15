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

from helper.gsheet.gsheet_util import *
from helper.logger import *

def list_of_dict(g):
    l = g.set_index('process').to_dict('records')
    l = [{k: v for k, v in d.items() if v is not None}  for d in l]
    l = [{k: v for k, v in d.items() if v is not None}  for d in l]

    return l

class GsheetReader(object):
    WORKSHEETS = {
        'workflow':      {'start-col': 'A', 'end-col': 'H', 'numerize': True},
        'test-case':     {'start-col': 'B', 'end-col': 'G', 'numerize': True},
    }

    def __init__(self, config):
        self._config = config
        self._log = []
        self.start_time = int(round(time.time() * 1000))

    def __del__(self):
        self.end_time = int(round(time.time() * 1000))
        print("gsheet took {} seconds".format((self.end_time - self.start_time)/1000))

    def df_from_worksheet(self, ws_title):
        self.info('reading worksheet: {0}'.format(ws_title))
        ws = self._config['gsheet'].worksheet('title', ws_title)
        if self.WORKSHEETS[ws_title]['numerize']:
            return ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=True, start='{0}2'.format(self.WORKSHEETS[ws_title]['start-col']), end='{0}{1}'.format(self.WORKSHEETS[ws_title]['end-col'], ws.rows))
        else:
            return ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=False, start='{0}2'.format(self.WORKSHEETS[ws_title]['start-col']), end='{0}{1}'.format(self.WORKSHEETS[ws_title]['end-col'], ws.rows))

    def merge_into_case(self, ws_title, data):
        for case, case_data in data.items():
            if case in self._cases:
                self._cases[case][ws_title] = case_data

    def info(self, msg):
        self._log.append({'type': 'info', 'time': datetime.now().isoformat(), 'msg': msg})

    def warn(self, msg):
        self._log.append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': msg})

    def error(self, msg):
        self._log.append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': msg})
