#!/usr/bin/env python
'''
'''
from helper.xlsx.xlsx_log_writer import XlsxLogWriter

class Login(XlsxLogWriter):

    def write(self, log):
        super().write(log)
