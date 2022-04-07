#!/usr/bin/env python
'''
'''
from helper.xlsx.xlsx_log_writer import XlsxLogWriter

class AwUserCreationRequest(XlsxLogWriter):

    def write(self, log):
        super().write(log)
