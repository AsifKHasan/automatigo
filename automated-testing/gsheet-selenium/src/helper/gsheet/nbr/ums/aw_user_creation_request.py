#!/usr/bin/env python
'''
'''

from helper.gsheet.gsheet_reader import GsheetReader

WS_LIST = {
    'aw-user-creation-request':    {'start-col': 'B', 'end-col': 'U', 'data': 'scalar', 'numerize': False},
}

class AwUserCreationRequest(GsheetReader):

    def read_gsheet(self):
        return super().read_gsheet(WS_LIST)
