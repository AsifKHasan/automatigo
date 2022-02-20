#!/usr/bin/env python3
'''
'''
import sys
import time
import traceback
from datetime import datetime
from helper.logger import Logger

class BaseWorker(Logger):

    def __init__(self, config, worker_name):
        super().__init__()
        self._label = worker_name
        self._config = config
        self.start_time = time.time()
        self.info('{0} ....'.format(self._label), console=True)

    def __del__(self):
        self.info('{0} done'.format(self._label), time_0=self.start_time, console=True)
