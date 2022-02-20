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

class UnitTestWorker(BaseWorker):

    def perform_work(self, data):
        self._whole_data = data
        self._data = data['unit-test']['configuration']
        self.run()

        return True, self._log

    def get_project_name(self, repo_name):
        git_repo_data = self._whole_data['git-repo']['configuration']
        for project in git_repo_data:
            for repo in git_repo_data[project]:
                if repo == repo_name:
                    return project


    def do_unit_test(self, repo, test_directory, test_command):
        error_code = os.system(f'cd {test_directory}; {test_command}')
        if error_code == 0:
            self.info(f'successfully ran unit test for repo "{repo}"', console=True)
        else:
            self.error(f'unit test failed for repo "{repo}"', console=True)


    def run(self):
        for repo in self._data:
            self.info(f'running unit test for repo "{repo}"' , console=True)
            project_name = self.get_project_name(repo)
            test_path = self._data[repo]['test-path']

            test_directory = self._config['dirs']['source-dir'] + '/'+ project_name + '/' + repo + '/' + test_path + '/'
            test_command = self._data[repo]['test-command']
            self.do_unit_test(repo, test_directory, test_command)












