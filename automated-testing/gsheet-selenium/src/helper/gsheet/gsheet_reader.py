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

class GsheetReader(object):

    def __init__(self, config):
        self._config = config
        self._log = []
        self.start_time = int(round(time.time() * 1000))

    def __del__(self):
        self.end_time = int(round(time.time() * 1000))
        print("gsheet took {} seconds".format((self.end_time - self.start_time)/1000))

    def info(self, msg):
        self._log.append({'type': 'info', 'time': datetime.now().isoformat(), 'msg': msg})

    def warn(self, msg):
        self._log.append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': msg})

    def error(self, msg):
        self._log.append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': msg})
