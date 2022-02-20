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

class CodeSanityWorker(BaseWorker):

    def perform_work(self, data):
        self._data = data['code-sanity']['configuration']

        return True, self._log
