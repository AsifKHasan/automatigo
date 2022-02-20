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

class DatabaseSchemaWorker(BaseWorker):

    def perform_work(self, data):
        self._data = data['database-schema']['configuration']

        return True, self._log
