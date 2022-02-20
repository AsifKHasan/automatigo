#!/usr/bin/env python3
'''
'''
import time
from datetime import datetime

class Logger(object):

    _log = None
    current_context_0 = None
    current_context_1 = None
    print_prefix = ''

    def debug(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('debug', msg, context_0, context_1, time_0, time_1, console)

    def info(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('info', msg, context_0, context_1, time_0, time_1, console)

    def warn(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('warn', msg, context_0, context_1, time_0, time_1, console)

    def error(self, msg, context_0=None, context_1=None, time_0=None, time_1=None, console=False):
        self.log('error', msg, context_0, context_1, time_0, time_1, console)

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

            print(self.print_prefix + '{0} {1:<6} {2}'.format(data['time'], data['type'], data['msg']))

            if 'elapsed_from_1' in data:
                print(self.print_prefix + '.. this activity : {0} seconds'.format(data['elapsed_from_1']))

            if 'elapsed_from_0' in data:
                print(self.print_prefix + '.. total elapsed : {0} seconds'.format(data['elapsed_from_0']))

            # print()

    def __init__(self):
        self._log = []
