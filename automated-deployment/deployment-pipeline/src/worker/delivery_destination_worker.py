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

class DeliveryDestinationWorker(BaseWorker):

    def perform_work(self, data):
        self._whole_data = data 
        self._data = data['delivery-destination']['configuration']
        self.run()
        return True, self._log

    def run(self):
        self.error(self._data)
        None