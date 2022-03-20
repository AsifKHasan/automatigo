#!/usr/bin/env python3
'''
'''
from helper.xlsx.xlsx_writer import XlsxLogWriter

class CreateMeetingXlsxLogWriter(XlsxLogWriter):
    
    def write(self, log):
        super().write(log)
