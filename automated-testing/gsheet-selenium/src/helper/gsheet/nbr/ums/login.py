#!/usr/bin/env python
'''
'''

from helper.gsheet.gsheet_reader import GsheetReader

WS_LIST = {
    'login':    {'start-col': 'B', 'end-col': 'D', 'data': 'scalar', 'numerize': True},
}

class Login(GsheetReader):

    def read_gsheet(self):
        return super().read_gsheet(WS_LIST)
