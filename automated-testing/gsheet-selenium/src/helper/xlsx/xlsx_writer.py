#!/usr/bin/env python3
'''
'''
import os
import sys
import json
import time
import datetime
import xlsxwriter

from helper.logger import *

class XlsxLogWriter(object):

    def worksheet_formats(self):
        # formats
        self.cell_format = {}
        self.cell_format['center'] = self._workbook.add_format({'align': 'center', 'font_name': 'Calibri', 'bold': False, 'font_size': 10, 'valign': 'vcenter'})
        self.cell_format['left'] = self._workbook.add_format({'align': 'left', 'font_name': 'Calibri', 'bold': False, 'font_size': 10, 'valign': 'vcenter'})

        self.red_fill = self._workbook.add_format({'bg_color': 'F4CCCC'})
        self.yellow_fill = self._workbook.add_format({'bg_color': 'FFF1BF'})
        self.gray_fill = self._workbook.add_format({'bg_color': 'E0E0E0'})
        self.bold_font = self._workbook.add_format({'bold': True})

        self.bottom_border = self._workbook.add_format({'bottom': 2, 'bottom_color': '080808'})

    def __init__(self, config):
        self.start_time = int(round(time.time() * 1000))
        self._config = config
        self._workbook = xlsxwriter.Workbook(self._config['files']['test-log-xlsx'])

        self.worksheet_formats()

    def __del__(self):
        if self._workbook:
            self._workbook.close()

        self.end_time = int(round(time.time() * 1000))
        info("Log-writer took {} seconds".format((self.end_time - self.start_time)/1000))
