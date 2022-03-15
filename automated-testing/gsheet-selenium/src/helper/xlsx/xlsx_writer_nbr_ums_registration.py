#!/usr/bin/env python3
'''
'''
import json
import time
import datetime
import xlsxwriter

from helper.xlsx.xlsx_writer import XlsxLogWriter
from helper.logger import *

headers = [
    ('A',  1, '#'             , 'center'  ,   5),
    ('B',  2, 'log-time'      , 'left'    ,  25),
    ('C',  3, 'log-level'     , 'left'    ,   8),
    ('D',  4, 'log-msg'       , 'left'    , 100),
    ('E',  5, 'activity-time' , 'center'  ,  12),
    ('F',  6, 'elapsed-time'  , 'center'  ,  12)
]

class NbrUmsRegistrationXlsxLogWriter(XlsxLogWriter):

    def write(self, log):
        self._log = log

        for work in self._log:
            self.write_worksheet(work, self._log[work])

    def write_worksheet(self, work_name, work_log):
        ws = self._workbook.add_worksheet(work_name)
        for i in range(0, len(headers)):
            ws.set_column('{0}:{0}'.format(headers[i][0]), headers[i][4], self.cell_format[headers[i][3]])
            ws.write(1, headers[i][1] - 1, headers[i][2])

        # freeze and hide
        ws.write('A1', '-')
        ws.freeze_panes('A3')
        ws.set_default_row(hide_unused_rows=True)
        ws.set_column('G:XFD', None, None, {'hidden': True})

        # write the data, data can be list of logs under work directly or list of Logs under dicts
        # we start writing from row 2
        self._current_row = 2
        if isinstance(work_log, dict):
            for process in work_log:
                self.write_process_block(ws, process, work_log[process])

        elif isinstance(work_log, list):
            for log_line in work_log:
                self.write_log_line(ws, log_line)

        # conditional formatting
        ws.conditional_format('A3:G{0}'.format(self._current_row), {'type': 'formula', 'criteria': '=$C3="warn"', 'format': self.yellow_fill})
        ws.conditional_format('A3:G{0}'.format(self._current_row), {'type': 'formula', 'criteria': '=$C3="error"', 'format': self.red_fill})

    def write_process_block(self, ws, process_name, process_log):
        merge_format = self._workbook.add_format({'align': 'left', 'bg_color': 'E0E0E0'})
        ws.merge_range('B{0}:F{0}'.format(self._current_row + 1), process_name, merge_format)
        self._current_row = self._current_row + 1
        for log_line in process_log:
            self.write_log_line(ws, log_line)

    def write_log_line(self, ws, log_line):
        ws.write(self._current_row, 1, log_line['time'])
        ws.write(self._current_row, 2, log_line['type'])
        ws.write(self._current_row, 3, log_line['msg'])

        if 'this-activity' in log_line:
            ws.write(self._current_row, 4, log_line['this-activity'])

        if 'elapsed' in log_line:
            ws.write(self._current_row, 5, log_line['elapsed'])

        self._current_row = self._current_row + 1
