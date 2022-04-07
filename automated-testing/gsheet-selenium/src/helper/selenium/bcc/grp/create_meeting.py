#!/usr/bin/env python
'''
'''

from datetime import datetime
from helper.selenium.selenium_driver import SeleniumDriver
from helper.utils import *


class CreateMeeting(SeleniumDriver):

    def login_data(self, case):
        return {'user-id': case['user-id'], 'password': case['password']}

    def entry_basic_info_data(self, case):
        data = case['basic-info']
        data['start-time-minute'] = convert_to_degree(data['start-time-minute'])
        data['end-time-minute'] = convert_to_degree(data['end-time-minute'])

        return data

    def entry_agenda_data(self, case):
        return case['agenda']

    def entry_key_personnel_data(self, case):
        data = case['key-personnel']
        data['member-secretary-search-text'] = get_part_of_text(data['member-secretary'])

        if data['chairperson'] is not None:
            data['chairperson-search-text'] = get_part_of_text(data['chairperson'])
        else:
            data['chairperson-search-text'] = None

        if data['chief-guest'] is not None:
            data['chief-guest-search-text'] = get_part_of_text(data['chief-guest'])
        else:
            data['chief-guest-search-text'] = None

        return data

    def entry_attendee_data(self, case):
        return case['attendee']

    def generate_notice_data(self, case):
        return {'notice-template': case['notice-template']}
