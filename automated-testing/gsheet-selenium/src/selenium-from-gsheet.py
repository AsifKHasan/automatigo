#!/usr/bin/env python3
'''
usage:
./selenium-from-gsheet.py --config '../conf/config.yml'
python selenium-from-gsheet.py --config "../conf/config.yml"
'''
import os
import sys
import time
import yaml
import json
import platform
import argparse
import importlib
import traceback
from datetime import datetime

from helper.gsheet.gsheet_helper import GsheetHelper

class SeleniumFromGsheet(object):

    def __init__(self, config_path):
        self.start_time = int(round(time.time() * 1000))
        self._config_path = os.path.abspath(config_path)
        self._data = {}

    def run(self):
        self.set_up()

        # read the test data from gsheet
        # gsheet-helper
        self._gsheet_helper = GsheetHelper()
        self._CONFIG['context'] = self._gsheet_helper.init(self._CONFIG)

        self._gsheet_log = []
        test_case_reader = getattr(importlib.import_module(self._CONFIG['test']['data']['module']), self._CONFIG['test']['data']['class'])
        self._gsheet_reader = test_case_reader(self._CONFIG['context'])
        try:
            try:
                self._data, self._gsheet_log = self._gsheet_reader.read_gsheet(self._CONFIG['context'])
            except Exception as e:
                self._gsheet_log.append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
                traceback.print_exc()
        finally:
            del self._gsheet_reader
            self.save_json(self._CONFIG['files']['gsheet-log-json'], self._gsheet_log)

        self.save_json(self._CONFIG['files']['output-json'], self._data)

        # drive the test through Selenium
        self._selenium_log = {'-': []}
        test_case_driver = getattr(importlib.import_module(self._CONFIG['test']['driver']['module']), self._CONFIG['test']['driver']['class'])
        self._selenium_driver = test_case_driver(self._CONFIG)
        try:
            try:
                self._selenium_log = self._selenium_driver.drive(self._data)
            except Exception as e:
                self._selenium_log['-'].append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
                traceback.print_exc()
        finally:
            del self._selenium_driver
            self.save_json(self._CONFIG['files']['selenium-log-json'], self._selenium_log)

        # generate xlsx test log
        test_log_writer = getattr(importlib.import_module(self._CONFIG['test']['log-writer']['module']), self._CONFIG['test']['log-writer']['class'])
        self._log_writer = test_log_writer(self._CONFIG)
        try:
            self._log_writer.write(self._selenium_log)
        finally:
            del self._log_writer

        self.tear_down()

    def set_up(self):
        # configuration
        self._CONFIG = yaml.load(open(self._config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        config_dir = os.path.dirname(self._config_path)

        self._CONFIG['dirs']['output-dir'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['dirs']['output-dir']))
        self._CONFIG['dirs']['temp-dir'] = os.path.abspath('{0}/tmp'.format(self._CONFIG['dirs']['output-dir']))
        if not os.path.exists(self._CONFIG['dirs']['temp-dir']):
            os.makedirs(self._CONFIG['dirs']['temp-dir'])

        self._CONFIG['files']['google-cred'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['files']['google-cred']))
        self._CONFIG['files']['output-json'] = os.path.abspath('{0}/{1}'.format(self._CONFIG['dirs']['output-dir'], self._CONFIG['files']['output-json']))
        self._CONFIG['files']['gsheet-log-json'] = os.path.abspath('{0}/{1}.log.json'.format(self._CONFIG['dirs']['output-dir'], self._CONFIG['test']['data']['gsheet']))
        self._CONFIG['files']['selenium-log-json'] = os.path.abspath('{0}/{1}.log.json'.format(self._CONFIG['dirs']['output-dir'], self._CONFIG['test']['case']))
        self._CONFIG['files']['test-log-xlsx'] = os.path.abspath('{0}/{1}.xlsx'.format(self._CONFIG['dirs']['output-dir'], self._CONFIG['test']['case']))

        # the os platform Windows, Linux, Darwin etc.
        self._CONFIG['platform'] = platform.system()

    def save_json(self, target_file_path, data_to_save):
        with open(target_file_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(data_to_save, sort_keys=False, indent=4, ensure_ascii=False))

    def tear_down(self):
        self.end_time = int(round(time.time() * 1000))
        print("script took {} seconds".format((self.end_time - self.start_time)/1000))

if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--config", required=True, help="configuration yml path")
    args = vars(ap.parse_args())

    generator = SeleniumFromGsheet(args["config"])
    generator.run()
