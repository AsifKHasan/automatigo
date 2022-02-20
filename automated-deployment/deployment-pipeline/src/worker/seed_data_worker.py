#!/usr/bin/env python3
'''
'''
import os
import sys
import time
import shutil
import traceback
from datetime import datetime

from worker.base_worker import BaseWorker

class SeedDataWorker(BaseWorker):

    def perform_work(self, data):
        self._data = data['seed-data']['configuration']

        return True, self._log
