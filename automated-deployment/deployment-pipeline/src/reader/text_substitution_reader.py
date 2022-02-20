#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'text-substitution':      {'start-col': 'B', 'end-col': 'D', 'numerize': True}
}

CHILD_WORKSHEET = {
    'repos': {'start-col': 'B', 'end-col': 'E', 'numerize': True},
    'placeholder': {'start-col': 'A', 'end-col': 'B', 'numerize': True}
}

class TextSubstitutionReader(GsheetReader):

    _label = 'text-substitution configuration data from gsheet'

    def read(self):

        df = self.df_from_worksheet('text-substitution', WORKSHEETS['text-substitution'])
        df = df.where((pd.notnull(df)), None)
        df = df[df['process'] == 'Yes']
        data = df.set_index('sheet').T.to_dict('dict')

        for sheet_name in data:
            data[sheet_name]['data'] = self.read_sheet(sheet_name, data[sheet_name]['worksheet'])

        return data, self._log

    def read_sheet(self, sheet_name, worksheet_name):
        # open the sheet, read the wowrksheet in 'worksheet' key
        gsheet = self._config['google-authorization']['_G'].open(sheet_name)
        ws = gsheet.worksheet('title', worksheet_name)
        df = ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=CHILD_WORKSHEET['repos']['numerize'], start='{0}2'.format(CHILD_WORKSHEET['repos']['start-col']), end='{0}{1}'.format(CHILD_WORKSHEET['repos']['end-col'], ws.rows))
        df = df[df['repo'].isin(self._pipeline_data['git-repo']['enabled_repositories'])]
        sheet_data = df.set_index('repo').T.to_dict('dict')

        for worksheet_name in sheet_data:
            result = self.read_worksheet(gsheet, worksheet_name)

            if result:
                sheet_data[worksheet_name]['placeholders'] = result

        return sheet_data

    def read_worksheet(self, gsheet, worksheet_name):
        ws = gsheet.worksheet('title', worksheet_name)
        df = ws.get_as_df(has_header=True, index_colum=None, empty_value=None, numerize=CHILD_WORKSHEET['placeholder']['numerize'], start='{0}2'.format(CHILD_WORKSHEET['placeholder']['start-col']), end='{0}{1}'.format(CHILD_WORKSHEET['placeholder']['end-col'], ws.rows))
        worksheet_data = df.set_index('placeholder').T.to_dict('dict')

        return worksheet_data
