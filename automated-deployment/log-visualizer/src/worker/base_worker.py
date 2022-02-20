#!/usr/bin/env python3
'''
'''
import sys
import time
import traceback
from datetime import datetime
from helper.logger import Logger

class BaseWorker(Logger):

    _worker_label = None
    _worker_config = None
    _global_context = None
    _start_time = None
    _is_running = None

    def __init__(self, worker_label, worker_config, global_context):
        super().__init__()
        self._worker_label = worker_label
        self._worker_config = worker_config
        self._global_context = global_context
        self._start_time = time.time()
        self.info('worker: {0} CREATED   ..'.format(self._worker_label), console=True)

    def __del__(self):
        self.info('worker: {0} DESTROYED ..'.format(self._worker_label), time_0=self._start_time, console=True)

    def start(self):
        self._is_running = True
        self.info('worker: {0} started  ...'.format(self._worker_label), time_0=self._start_time, console=True)

    def stop(self):
        self._is_running = False
        self.info('worker: {0} stopped  ...'.format(self._worker_label), time_0=self._start_time, console=True)

    def is_running(self):
        return self._is_running

    def process(self, task_data):
        pass
