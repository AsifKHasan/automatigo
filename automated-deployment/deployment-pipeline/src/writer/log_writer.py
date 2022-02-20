#!/usr/bin/env python3
'''
'''
import json
import time
import datetime
import xlsxwriter

from writer.xlsx_writer import XlsxWriter

HEADERS = {
    'A' : {'col-num': 1, 'header-text': '#'             , 'halign': 'center'  , 'width':    5, 'wrap': False , 'data-key': None              },
    'B' : {'col-num': 2, 'header-text': 'log-time'      , 'halign': 'left'    , 'width':   25, 'wrap': False , 'data-key': 'time'            },
    'C' : {'col-num': 3, 'header-text': 'log-level'     , 'halign': 'left'    , 'width':    8, 'wrap': False , 'data-key': 'type'            },
    'D' : {'col-num': 4, 'header-text': 'context'       , 'halign': 'left'    , 'width':   20, 'wrap': False , 'data-key': 'context_0'       },
    'E' : {'col-num': 5, 'header-text': 'sub-context'   , 'halign': 'left'    , 'width':   20, 'wrap': False , 'data-key': 'context_1'       },
    'F' : {'col-num': 6, 'header-text': 'log-msg'       , 'halign': 'left'    , 'width':  100, 'wrap': True  , 'data-key': 'msg'             },
    'G' : {'col-num': 7, 'header-text': 'activity-time' , 'halign': 'center'  , 'width':   12, 'wrap': False , 'data-key': 'elapsed_from_1'  },
    'H' : {'col-num': 8, 'header-text': 'elapsed-time'  , 'halign': 'center'  , 'width':   12, 'wrap': False , 'data-key': 'elapsed_from_0'  }
}

HEADER_ROW = 1

class LogWriter(XlsxWriter):

    def write(self, log):
        self._log = log

        for group in self._log:
            self.write_worksheet(group, self._log[group])

    def write_worksheet(self, group_name, group_log):
        ws = self._workbook.add_worksheet(group_name)
        for col, col_spec in HEADERS.items():
            format = self._workbook.add_format(self._default_format_spec)
            format.set_align(col_spec['halign'])
            if col_spec['wrap']:
                format.set_text_wrap()

            ws.set_column('{0}:{0}'.format(col), col_spec['width'], format)
            ws.write(HEADER_ROW, col_spec['col-num'] - 1, col_spec['header-text'], self.bold_font)

        # freeze and hide
        ws.write('A1', '-')
        ws.freeze_panes('A3')
        ws.set_default_row(hide_unused_rows=True)
        ws.set_column('I:XFD', None, None, {'hidden': True})

        # write the data, data can be list of logs under work directly or list of Logs under dicts
        # we start writing from the row below HEADER_ROW
        self._current_row = HEADER_ROW + 1
        for log_line in group_log:
            self.write_log_line(ws, log_line)

        # conditional formatting
        ws.conditional_format('A3:H{0}'.format(self._current_row), {'type': 'formula', 'criteria': '=$C3="warn"', 'format': self.yellow_fill})
        ws.conditional_format('A3:H{0}'.format(self._current_row), {'type': 'formula', 'criteria': '=$C3="error"', 'format': self.red_fill})

    def write_log_line(self, ws, log_line):
        for col, col_spec in HEADERS.items():
            if col_spec['data-key'] is not None and col_spec['data-key'] in log_line:
                ws.write(self._current_row, col_spec['col-num'] - 1, log_line[col_spec['data-key']])

        self._current_row = self._current_row + 1
