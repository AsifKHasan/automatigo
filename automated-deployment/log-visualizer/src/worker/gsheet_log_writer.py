#!/usr/bin/env python3
'''
'''
import pygsheets
from pygsheets.custom_types import *

from helper.gsheet_util import *
from worker.base_worker import BaseWorker

COLUMN_SPEC = {
    'table-borders': {
        'top':    { "style": 'SOLID', "color": hex_to_rgba('808080FF')},
        'right':  { "style": 'SOLID', "color": hex_to_rgba('808080FF')},
        'bottom': { "style": 'SOLID', "color": hex_to_rgba('808080FF')},
        'left':   { "style": 'SOLID', "color": hex_to_rgba('808080FF')}
    },
    'columns': {
        'A': {'col-num': 0, 'header-text': '#'             , 'halign': 'CENTER' , 'width':   40, 'wrap': False , 'number-format': {'type': 'TEXT'}                       , 'header-bg-color': 'E0E0E0FF', 'data-key': None              },
        'B': {'col-num': 1, 'header-text': 'log-time'      , 'halign': 'LEFT'   , 'width':  170, 'wrap': False , 'number-format': {'type': 'TEXT'}                       , 'header-bg-color': 'E0E0E0FF', 'data-key': 'time'            },
        'C': {'col-num': 2, 'header-text': 'log-level'     , 'halign': 'LEFT'   , 'width':   60, 'wrap': False , 'number-format': {'type': 'TEXT'}                       , 'header-bg-color': 'E0E0E0FF', 'data-key': 'type'            },
        'D': {'col-num': 3, 'header-text': 'context'       , 'halign': 'LEFT'   , 'width':   70, 'wrap': False , 'number-format': {'type': 'TEXT'}                       , 'header-bg-color': 'E0E0E0FF', 'data-key': 'context_0'       },
        'E': {'col-num': 4, 'header-text': 'sub-context'   , 'halign': 'LEFT'   , 'width':  180, 'wrap': False , 'number-format': {'type': 'TEXT'}                       , 'header-bg-color': 'E0E0E0FF', 'data-key': 'context_1'       },
        'F': {'col-num': 5, 'header-text': 'log-msg'       , 'halign': 'LEFT'   , 'width':  900, 'wrap': True  , 'number-format': {'type': 'TEXT'}                       , 'header-bg-color': 'E0E0E0FF', 'data-key': 'msg'             },
        'G': {'col-num': 6, 'header-text': 'activity-time' , 'halign': 'CENTER' , 'width':   80, 'wrap': False , 'number-format': {'type': 'NUMBER', 'pattern': '0.00'}  , 'header-bg-color': 'E0E0E0FF', 'data-key': 'elapsed_from_1'  },
        'H': {'col-num': 7, 'header-text': 'elapsed-time'  , 'halign': 'CENTER' , 'width':   80, 'wrap': False , 'number-format': {'type': 'NUMBER', 'pattern': '0.00'}  , 'header-bg-color': 'E0E0E0FF', 'data-key': 'elapsed_from_0'  }
    }
}

BGCOLOR_ERROR = 'F4CCCCFF'
BGCOLOR_WARN = 'FFF1BFFF'

class GsheetLogWriter(BaseWorker):

    def start(self):
        self.info('worker: {0} starting ...'.format(self._worker_label), time_0=self._start_time, console=True)

        if self.prepare_sheet():
            super().start()
        else:
            self.error('worker: {0} start failed ...'.format(self._worker_label), time_0=self._start_time, console=True)

        return self._is_running

    def stop(self):
        self.info('worker: {0} stopping ...'.format(self._worker_label), time_0=self._start_time, console=True)

        super().stop()

    def prepare_sheet(self):
        # authorize
        self._worker_config['google-authorization'] = authorize('{0}/{1}'.format(self._global_context['config-dir'], self._worker_config['args']['cred-json']))

        # open gsheet
        self._worker_config['gsheet'] = self._worker_config['google-authorization']['_G'].open(self._worker_config['args']['gsheet-name'])

        # add a worksheet
        self._current_ws = init_worksheet(self._worker_config['gsheet'], self._worker_config['args']['worksheet-name'], num_rows=3, num_cols=8, frozen_rows=2, frozen_cols=0, col_def=COLUMN_SPEC['columns'], index=1)

        # add conditional formatting for error and warn rows
        requests = []
        requests.append({
          'addConditionalFormatRule': {
            'rule': {
              'ranges': [range_object(self._current_ws, 2, self._current_ws.rows, 0, self._current_ws.cols)],
              'booleanRule': {
                'condition': {
                  'type': 'CUSTOM_FORMULA',
                  'values': [{
                    'userEnteredValue': '=$C:$C="error"'
                  }]
                },
                'format': {
                  'backgroundColor': hex_to_rgba(BGCOLOR_ERROR)
                }
              }
            },
            'index': 0
          }
        })

        requests.append({
          'addConditionalFormatRule': {
            'rule': {
              'ranges': [range_object(self._current_ws, 2, self._current_ws.rows, 0, self._current_ws.cols)],
              'booleanRule': {
                'condition': {
                  'type': 'CUSTOM_FORMULA',
                  'values': [{
                    'userEnteredValue': '=$C:$C="warn"'
                  }]
                },
                'format': {
                  'backgroundColor': hex_to_rgba(BGCOLOR_WARN)
                }
              }
            },
            'index': 1
          }
        })

        self._worker_config['gsheet'].custom_request(requests, None)

        self.info('worksheet: {0} initialized'.format(self._worker_label), time_0=self._start_time, console=True)

        return True

    '''
        task_data is a dict - time, type, context_0, context_1, msg, elapsed_from_1, elapsed_from_0
    '''
    def process(self, task_data):
        if task_data is None or not isinstance(task_data, dict):
            return

        requests = []
        # this goes in 3rd row always, we need the 3rd row inserted
        requests.append(insert_dimension_request(self._current_ws, 'ROWS', 2, 1, False))

        # now the values
        for _, col_spec in COLUMN_SPEC['columns'].items():
            if col_spec['data-key'] in task_data:
                requests.append(format_range_request(self._current_ws, 2, 3, col_spec['col-num'], col_spec['col-num'] + 1, user_entered_value=task_data[col_spec['data-key']]))

        self._worker_config['gsheet'].custom_request(requests, None)
