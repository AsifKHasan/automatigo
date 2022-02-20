#!/usr/bin/env python3
'''
'''
import os
import sys
import time
import shutil
import traceback
from datetime import datetime

from worker.base_worker import BaseWorker

class TextSubstitutionWorker(BaseWorker):

    def perform_work(self, data):
        self._whole_data = data
        self._data = data['text-substitution']['configuration']
        self.run()

        return True, self._log

    def get_project_name(self, repo_name):
        git_repo_data = self._whole_data['git-repo']['configuration']
        for project in git_repo_data:
            for repo in git_repo_data[project]:
                if repo == repo_name:
                    return project

    def substitute_properties(self, repo, repo_clone_directory, placeholder, placeholder_value):
        error_code = os.system(f'cd {repo_clone_directory}; grep -rl "{placeholder}" | xargs sed -i "s|{placeholder}|{placeholder_value}|g"')
        if error_code == 0:
            self.info(f'successfully replaced placeholder {placeholder} for repo "{repo}" ', console=True)
        else:
            self.warn(f'could not replace placeholder {placeholder} for repo "{repo}"', console=True)

    def run(self):
        for datasheet in self._data:
            for repo in self._data[datasheet]['data']:
                project_name = self.get_project_name(repo)
                repo_clone_directory = self._config['dirs']['source-dir'] + '/'+ project_name + '/' + repo
                placeholder_data = self._data[datasheet]['data'][repo]['placeholders']
                for placeholder in placeholder_data:
                    placeholder_value = placeholder_data[placeholder]['value']
                    self.substitute_properties(repo, repo_clone_directory, placeholder, placeholder_value)






