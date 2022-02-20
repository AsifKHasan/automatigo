#!/usr/bin/env python3
'''
'''
import time
from datetime import datetime
from termcolor import colored

from rsmq import RedisSMQ

log_color = {
    'ERROR': {'color': 'red',    'highlight': None, 'attrs': ['bold']},
    'WARN':  {'color': 'yellow', 'highlight': None, 'attrs': ['bold']},
    'INFO':  {'color': 'white',  'highlight': None, 'attrs': None},
    'DEBUG': {'color': 'green',  'highlight': None, 'attrs': None}
}

class Logger(object):

    current_context_0 = None
    current_context_1 = None
    print_prefix = ''
    _mq_for_log = None
    _log = None

    def debug(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('DEBUG', msg, context_0, context_1, time_0, time_1, console)

    def info(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('INFO', msg, context_0, context_1, time_0, time_1, console)

    def warn(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('WARN', msg, context_0, context_1, time_0, time_1, console)

    def error(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('ERROR', msg, context_0, context_1, time_0, time_1, console)

    def log(self, level, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        now = time.time()
        data = {'type': level, 'time': datetime.now().isoformat(), 'msg': msg}
        if context_0:
            data['context_0'] = context_0
            self.print_prefix = ' ' * 4
        else:
            self.print_prefix = ''

        if context_1:
            data['context_1'] = context_1

        if time_0: data['elapsed_from_0'] = now - time_0
        if time_1: data['elapsed_from_1'] = now - time_1

        if context_0 != self.current_context_0:
            self.current_context_0 = context_0
            print_context_0 = True
        else:
            print_context_0 = False

        if context_1 != self.current_context_1:
            self.current_context_1 = context_1
            print_context_1 = True
        else:
            print_context_1 = False

        self._log.append(data)

        if console:
            if 'context_0' in data and print_context_0:
                s = data['context_0']
                if 'context_1' in data:
                    s = '{0} -> {1}'.format(s, data['context_1'])

                print(s)

            text = self.print_prefix + '{0} {1:<6} {2}'.format(data['time'], data['type'], data['msg'])
            print(colored(text, log_color[data['type']]['color'], log_color[data['type']]['highlight'], attrs=log_color[data['type']]['attrs']))

            if 'elapsed_from_1' in data:
                text = self.print_prefix + '.. this activity : {0} seconds'.format(data['elapsed_from_1'])
                print(colored(text, 'blue', 'on_grey'))

            if 'elapsed_from_0' in data:
                text = self.print_prefix + '.. total elapsed : {0} seconds'.format(data['elapsed_from_0'])
                print(colored(text, 'blue', 'on_grey'))

        if 'mq' in self._config and self._config['mq']:
            self._config['mq'].sendMessage(delay=0).message(data).execute()

    def __init__(self):
        self._log = []
