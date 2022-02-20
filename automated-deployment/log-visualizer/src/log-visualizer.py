#!/usr/bin/env python3
'''
usage:
./log-visualizer.py --config '../conf/config.yml'
python log-visualizer.py --config "../conf/config.yml"
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

class LogVisualizer(object):

    def __init__(self, config_path):
        self.start_time = time.time()
        self._config_path = os.path.abspath(config_path)
        self._active_workers = {}

    def run_worker(self, worker_name, worker_config):
        if not all(key in worker_config for key in ['active', 'module', 'class']):
            print('worker {0} missing one of the keys [active, module, class]'.format(worker_name))
            return False

        if not worker_config['active']:
            print('worker {0} is inactive, it will not be started'.format(worker_name))
            return False

        worker_obj = getattr(importlib.import_module(worker_config['module']), worker_config['class'])
        worker = worker_obj(worker_name, worker_config, self._CONFIG)

        try:
            result = worker.start()
            # we keep the reference of the worker for use by others
            self._active_workers[worker_name] = worker
        except Exception as e:
            traceback.print_exc()
            return False

        return result

    def run(self):
        self.set_up()

        # run the workers
        for worker_name in self._CONFIG['workers']:
            if self._CONFIG['workers'][worker_name]:
                if not self.run_worker(worker_name, self._CONFIG['workers'][worker_name]):
                    break

        print('waiting for message ....')
        while True:
            pass

        self.tear_down()

    def set_up(self):
        # read configuration
        self._CONFIG = yaml.load(open(self._config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        self._CONFIG['config-dir'] = os.path.dirname(self._config_path)
        self._CONFIG['active-workers'] = self._active_workers

    def tear_down(self):
        self.end_time = time.time()
        print("script took {} seconds".format(time.time() - self.start_time))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--config", required=True, help="configuration yml path")
    args = vars(ap.parse_args())

    generator = LogVisualizer(args["config"])
    generator.run()
