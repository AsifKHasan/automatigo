#!/usr/bin/env python
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

WORKSHEETS = {
        'workflow':      {'start-col': 'A', 'end-col': 'H', 'numerize': True},
        'test-case':     {'start-col': 'A', 'end-col': 'E', 'numerize': True},
    }

def list_of_dict(g):
    l = g.set_index('process').to_dict('records')
    l = [{k: v for k, v in d.items() if v is not None}  for d in l]
    l = [{k: v for k, v in d.items() if v is not None}  for d in l]

    return l

class GsheetReader(object):

    '''
    '''
    def __init__(self, config):
        self._config = config
        self._log = []
        self.start_time = int(round(time.time() * 1000))


    '''
    '''
    def __del__(self):
        self.end_time = int(round(time.time() * 1000))
        info(f"gsheet took {(self.end_time - self.start_time)/1000} seconds")


    '''
    '''
    def df_from_worksheet(self, ws_title, ws_spec):
        self.info(f"reading worksheet: {ws_title}")
        ws = self._config['gsheet'].worksheet('title', ws_title)
        if ws_spec['numerize']:
            return ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=True, start=f"{ws_spec['start-col']}2", end=f"{ws_spec['end-col']}{ws.rows}")
        else:
            return ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=False, start=f"{ws_spec['start-col']}2", end=f"{ws_spec['end-col']}{ws.rows}")


    '''
    '''
    def merge_into_case(self, ws_title, data):
        for case, case_data in data.items():
            if case in self._cases:
                self._cases[case][ws_title] = case_data


    '''
    '''
    def read_gsheet(self, ws_dict):
        # a worksheet named *workflow* must be there
        ws_name = 'workflow'
        df = self.df_from_worksheet(ws_name, WORKSHEETS[ws_name])
        # forward fill
        df.process = pd.Series(df.process).fillna(method='ffill')
        df.work = pd.Series(df.work).fillna(method='ffill')
        df = df[df['action'].notnull()]
        df = df[df['skip'] != 'Yes']
        df = df.where((pd.notnull(df)), None)
        self._workflow = df.groupby('work', sort=False).apply(lambda g: g.set_index('work').groupby('process', sort=False).apply(lambda g: list_of_dict(g)).to_dict()).to_dict()

        # a worksheet named *test-case* must be there
        ws_name = 'test-case'
        df = self.df_from_worksheet(ws_name, WORKSHEETS[ws_name])
        df = df[df['skip'] != 'Yes']
        self._cases = df.set_index('case').T.to_dict('dict')

        # read the other worksheets
        for ws_name, ws_spec in ws_dict.items():
            df = self.df_from_worksheet(ws_name, ws_spec)
            df = df[df['case'].isin(self._cases.keys())]
            if ws_spec['data'] == 'scalar':
                data = df.set_index('case').T.to_dict('dict')

            elif ws_spec['data'] == 'tabular':
                data = df.groupby('case', sort=False).apply(lambda g: g.set_index('case').to_dict('records')).to_dict()

            else:
                continue

            self.merge_into_case(ws_name, data)

        return {'test-case': self._cases, 'workflow': self._workflow}, self._log


    '''
    '''
    def info(self, msg):
        self._log.append({'type': 'info', 'time': datetime.now().isoformat(), 'msg': msg})


    '''
    '''
    def warn(self, msg):
        self._log.append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': msg})


    '''
    '''
    def error(self, msg):
        self._log.append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': msg})
