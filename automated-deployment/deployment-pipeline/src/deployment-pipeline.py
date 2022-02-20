#!/usr/bin/env python3
'''
usage:
./deployment-pipeline.py --config '../conf/config.yml'
python deployment-pipeline.py --config "../conf/config.yml"
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
from termcolor import colored

from rsmq import RedisSMQ

class DeploymentPipeline(object):

    def __init__(self, config_path):
        self.start_time = time.time()
        self._config_path = os.path.abspath(config_path)
        self._log = {'pipeline-reader': []}
        self._data = {}

    def run(self):
        self.set_up()

        # read the pipeline
        if not self.read_pipeline():
            return

        self.init_mq()

        # run the workers
        for stage, stage_spec in self._pipeline.items():
            if not self.run_worker(stage, stage_spec):
                break

        self.save_json(self._CONFIG['files']['log-json'], self._log)

        self.write_log()

        self.tear_down()

    def set_up(self):
        # configuration
        self._CONFIG = yaml.load(open(self._config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        config_dir = os.path.dirname(self._config_path)

        self._CONFIG['config-dir'] = config_dir

        self._CONFIG['dirs']['template-dir'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['dirs']['template-dir']))
        self._CONFIG['dirs']['output-dir'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['dirs']['output-dir']))
        if not os.path.exists(self._CONFIG['dirs']['output-dir']):
            os.makedirs(self._CONFIG['dirs']['output-dir'])

        self._CONFIG['dirs']['log-dir'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['dirs']['log-dir']))
        if not os.path.exists(self._CONFIG['dirs']['log-dir']):
            os.makedirs(self._CONFIG['dirs']['log-dir'])

        self._CONFIG['dirs']['image-dir'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['dirs']['image-dir']))
        if not os.path.exists(self._CONFIG['dirs']['image-dir']):
            os.makedirs(self._CONFIG['dirs']['image-dir'])

        self._CONFIG['files']['google-cred'] = os.path.abspath('{0}/{1}'.format(config_dir, self._CONFIG['files']['google-cred']))
        self._CONFIG['files']['output-json'] = os.path.abspath('{0}/{1}'.format(self._CONFIG['dirs']['output-dir'], self._CONFIG['files']['output-json']))
        self._CONFIG['files']['log-json'] = os.path.abspath('{0}/{1}'.format(self._CONFIG['dirs']['log-dir'], self._CONFIG['files']['log-json']))

    def read_pipeline(self):
        pipeline_reader_obj = getattr(importlib.import_module(self._CONFIG['deployment']['configuration']['module']), self._CONFIG['deployment']['configuration']['class'])
        pipeline_reader = pipeline_reader_obj(self._CONFIG, None)
        try:
            pipeline_reader.init(self._CONFIG['deployment']['configuration']['gsheet'], self._CONFIG['files']['google-cred'])
            self._pipeline, self._log['pipeline-reader'] = pipeline_reader.read()
        except Exception as e:
            self._log['pipeline-reader'].append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
            traceback.print_exc()
            return False
        finally:
            if pipeline_reader: del pipeline_reader

        # read each stage data
        for stage, stage_spec in self._pipeline.items():
            self._log[stage] = []
            if stage_spec['read'] != 'Yes':
                self._log[stage].append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': 'reader : {0} read flag is off ... skipping'.format(stage)})
                continue

            if stage_spec['reader-module'] is None or stage_spec['reader-class'] is None:
                self._log[stage].append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': 'reader : {0} is not implemented yet'.format(stage)})
                continue

            reader_obj = getattr(importlib.import_module(stage_spec['reader-module']), stage_spec['reader-class'])
            reader = reader_obj(self._CONFIG, self._pipeline)
            try:
                self._pipeline[stage]['configuration'], self._log[stage] = reader.read()
            except Exception as e:
                self._log[stage].append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
                traceback.print_exc()
                return False
            finally:
                if reader: del reader

        self.save_json(self._CONFIG['files']['output-json'], self._pipeline)

        return True

    def init_mq(self):
        self._CONFIG['mq'] = None
        if 'enabled' not in self._CONFIG['mq-for-log']:
            print(colored('MQ not configured', 'yellow'))
            return

        if not self._CONFIG['mq-for-log']['enabled']:
            print(colored('MQ not active', 'yellow'))
            return

        try:
            queue = RedisSMQ(host=self._CONFIG['mq-for-log']['host'], port=self._CONFIG['mq-for-log']['port'], qname=self._CONFIG['mq-for-log']['queue-name'])
            queue.deleteQueue().exceptions(False).execute()

            # Create Queue with default visibility timeout of 20 and delay of 0
            queue.createQueue(delay=0).vt(20).execute()
            self._CONFIG['mq'] = queue
            print('MQ started')
        except Exception as e:
            traceback.print_exc()

    def run_worker(self, worker_name, worker_spec):
        if worker_spec['execute'] != 'Yes':
            self._log[worker_name].append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': 'worker : {0} execution flag is off ... skipping'.format(worker_name)})
            return True

        if worker_spec['worker-module'] is None or worker_spec['worker-class'] is None:
            self._log[worker_name].append({'type': 'warn', 'time': datetime.now().isoformat(), 'msg': 'worker : {0} is not implemented yet'.format(worker_name)})
            return True

        worker_obj = getattr(importlib.import_module(worker_spec['worker-module']), worker_spec['worker-class'])
        worker = worker_obj(self._CONFIG, worker_name)
        try:
            result, self._log[worker_name] = worker.perform_work(self._pipeline)
        except Exception as e:
            self._log[worker_name] = []
            self._log[worker_name].append({'type': 'error', 'time': datetime.now().isoformat(), 'msg': str(e)})
            traceback.print_exc()
            return False
        finally:
            if worker: del worker

        return result

    def write_log(self):
        writer_obj = getattr(importlib.import_module(self._CONFIG['deployment']['log-writer']['module']), self._CONFIG['deployment']['log-writer']['class'])
        log_writer = writer_obj(self._CONFIG, self._CONFIG['deployment']['log-writer']['args'])
        try:
            log_writer.write(self._log)
        finally:
            del log_writer

    def save_json(self, target_file_path, data_to_save):
        with open(target_file_path, "w", encoding='utf-8') as f:
            f.write(json.dumps(data_to_save, sort_keys=False, indent=4, ensure_ascii=False))

    def tear_down(self):
        self.end_time = time.time()
        print("script took {} seconds".format(time.time() - self.start_time))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--config", required=True, help="configuration yml path")
    args = vars(ap.parse_args())

    generator = DeploymentPipeline(args["config"])
    generator.run()
