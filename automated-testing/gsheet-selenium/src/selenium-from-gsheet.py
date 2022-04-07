#!/usr/bin/env python
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
from pathlib import Path
from datetime import datetime

from helper.gsheet.gsheet_helper import GsheetHelper
from helper.logger import *

class SeleniumFromGsheet(object):

    def __init__(self, config_path):
        self.start_time = int(round(time.time() * 1000))
        self._config_path = Path(config_path).resolve()
        self._data = {}

    def run(self):
        self.set_up()

        # authenticate with Google
        self._gsheet_helper = GsheetHelper()
        self._CONFIG['context'] = self._gsheet_helper.init(self._CONFIG)

        self._gsheet_log = []
        # read the test-spec gsheet
        test_spec_gsheet_reader = getattr(importlib.import_module(self._CONFIG['test-spec']['module'].format('gsheet')), self._CONFIG['test-spec']['class'])
        self._gsheet_reader = test_spec_gsheet_reader(self._CONFIG['context'])
        self._CONFIG['files']['gsheet-log-json'] = Path(f"{self._CONFIG['dirs']['output-dir']}/{self._CONFIG['test-spec']['spec-file']}.log.json")
        self._CONFIG['files']['output-json'] = Path(f"{self._CONFIG['dirs']['output-dir']}/{self._CONFIG['test-spec']['spec-file']}.data.json")
        try:
            try:
                self._data, self._gsheet_log = self._gsheet_reader.read_gsheet()
            except Exception as e:
                self._gsheet_log.append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
                traceback.print_exc()
        finally:
            del self._gsheet_reader
            self.save_json(self._CONFIG['files']['gsheet-log-json'], self._gsheet_log)

        self.save_json(self._CONFIG['files']['output-json'], self._data)

        if len(self._data['test-case'].keys()) == 0:
            warn(f"no test case to run")

        # drive the test through Selenium, do these for all selected cases
        for test_case_name in self._data['test-case'].keys():
            info(f"BEGIN test-case {test_case_name}")

            test_case_output_dir = Path(f"{self._CONFIG['dirs']['output-dir']}/{test_case_name}")
            test_case_tmp_dir = Path(f"{test_case_output_dir}/tmp")
            test_case_tmp_dir.mkdir(parents=True, exist_ok=True)
            selenium_log_json_path = Path(f"{test_case_output_dir}/{test_case_name}.log.json")
            test_log_xlsx_path = Path(f"{test_case_output_dir}/{test_case_name}.log.xlsx")

            self._selenium_log = {'-': []}
            test_spec_selenium_driver = getattr(importlib.import_module(self._CONFIG['test-spec']['module'].format('selenium')), self._CONFIG['test-spec']['class'])
            self._selenium_driver = test_spec_selenium_driver(self._CONFIG, test_case_tmp_dir)
            try:
                try:
                    self._selenium_log = self._selenium_driver.drive(test_case_name, self._data)
                except Exception as e:
                    self._selenium_log['-'].append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
                    traceback.print_exc()
            finally:
                del self._selenium_driver
                self.save_json(selenium_log_json_path, self._selenium_log)

            # generate xlsx test log
            test_spec_xlsx_log_writer = getattr(importlib.import_module(self._CONFIG['test-spec']['module'].format('xlsx')), self._CONFIG['test-spec']['class'])
            self._log_writer = test_spec_xlsx_log_writer(test_log_xlsx_path)
            try:
                self._log_writer.write(self._selenium_log)
            finally:
                del self._log_writer

            info(f"END   test-case {test_case_name}")

        # finally tear down everything
        self.tear_down()

    def set_up(self):
        # configuration
        self._CONFIG = yaml.load(open(self._config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        config_dir = self._config_path.parent

        self._CONFIG['test-spec']['spec-file'] = f"test-spec__{self._CONFIG['test-spec']['spec-file']}"
        self._CONFIG['dirs']['output-dir'] = Path(f"{config_dir}/{self._CONFIG['dirs']['output-dir']}/{self._CONFIG['test-spec']['spec-file']}")
        self._CONFIG['dirs']['output-dir'].mkdir(parents=True, exist_ok=True)

        self._CONFIG['files']['google-cred'] = Path(f"{config_dir}/{self._CONFIG['files']['google-cred']}")

        # the os platform Windows, Linux, Darwin etc.
        self._CONFIG['platform'] = platform.system()

    def save_json(self, target_file_path, data_to_save):
        with open(target_file_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(data_to_save, sort_keys=False, indent=4, ensure_ascii=False))

    def tear_down(self):
        self.end_time = int(round(time.time() * 1000))
        info(f"script took {(self.end_time - self.start_time)/1000} seconds")

if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--config", required=True, help="configuration yml path")
    args = vars(ap.parse_args())

    generator = SeleniumFromGsheet(args["config"])
    generator.run()
