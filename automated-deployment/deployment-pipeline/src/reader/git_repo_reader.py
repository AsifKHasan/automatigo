#!/usr/bin/env python3
'''
'''
import pandas as pd
from math import isnan

from reader.gsheet_reader import GsheetReader

WORKSHEETS = {
    'git-repo':      {'start-col': 'B', 'end-col': 'G', 'numerize': True}
}

class GitRepoReader(GsheetReader):

    _label = 'git-repo configuration data from gsheet'

    def read(self):

        df = self.df_from_worksheet('git-repo', WORKSHEETS['git-repo'])
        df['project'] = pd.Series(df['project']).fillna(method='ffill')
        df = df[df['repo'].notnull()]
        df = df[df['clone'] == 'Yes']
        df = df.where((pd.notnull(df)), None)
        data = df.groupby('project', sort=False)\
                .apply(lambda g: g[['repo', 'clone','branch', 'tag', 'url-pattern']].set_index('repo').T.to_dict('dict'))\
                .to_dict()

        enabled_repositories = []
        for project in data:
            for repo in data[project]:
                enabled_repositories.append(repo)
        self._pipeline_data['git-repo']['enabled_repositories']=enabled_repositories

        return data, self._log
