#!/usr/bin/env python
'''
'''

from helper.gsheet.gsheet_reader import GsheetReader

WS_LIST = {
    'basic-info':    {'start-col': 'B', 'end-col': 'O', 'data': 'scalar', 'numerize': False},
    'background':    {'start-col': 'B', 'end-col': 'D', 'data': 'tabular', 'numerize': True},
    'agenda':        {'start-col': 'B', 'end-col': 'D', 'data': 'tabular', 'numerize': True},
    'key-personnel': {'start-col': 'B', 'end-col': 'G', 'data': 'scalar', 'numerize': True},
    'attachment':    {'start-col': 'B', 'end-col': 'D', 'data': 'tabular', 'numerize': True},
    'attendee':      {'start-col': 'B', 'end-col': 'P', 'data': 'tabular', 'numerize': True},
}

class CreateMeetingGsheetReader(GsheetReader):

    def read_gsheet(self):
        return super().read_gsheet(WS_LIST)
