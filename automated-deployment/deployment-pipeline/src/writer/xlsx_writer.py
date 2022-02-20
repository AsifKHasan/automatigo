#!/usr/bin/env python3
'''
'''
import os
import sys
import json
import time
import datetime
import xlsxwriter

class XlsxWriter(object):

    def worksheet_formats(self):
        # formats
        self._default_format_spec = {'font_name': 'Calibri', 'bold': False, 'font_size': 10, 'valign': 'vcenter'}

        self.red_fill = self._workbook.add_format({'bg_color': 'F4CCCC'})
        self.yellow_fill = self._workbook.add_format({'bg_color': 'FFF1BF'})
        self.gray_fill = self._workbook.add_format({'bg_color': 'E0E0E0'})
        self.bold_font = self._workbook.add_format({'bold': True})

        self.bottom_border = self._workbook.add_format({'bottom': 2, 'bottom_color': '080808'})

    def __init__(self, config, args):
        self.start_time = time.time()
        self._CONFIG = config
        self._xlsx_path = os.path.abspath('{0}/{1}.xlsx'.format(self._CONFIG['dirs']['log-dir'], args['file-path']))

        self._workbook = xlsxwriter.Workbook(self._xlsx_path)

        self.worksheet_formats()

    def __del__(self):
        if self._workbook:
            self._workbook.close()

        print('log-writer took {} seconds'.format(time.time() - self.start_time))
