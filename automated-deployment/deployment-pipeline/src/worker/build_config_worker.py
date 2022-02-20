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

class BuildConfigWorker(BaseWorker):

    def perform_work(self, data):
        self._whole_data = data
        self._data = data['build-config']['configuration']
        self.run()
        return True, self._log

    def get_project_name(self, repo_name):
        git_repo_data = self._whole_data['git-repo']['configuration']
        for project in git_repo_data:
            for repo in git_repo_data[project]:
                if repo == repo_name:
                    return project

    def get_application_name(self, repo_name):
        application_name_data = self._whole_data['text-substitution']['configuration']
        for sheet in application_name_data:
            for repo in application_name_data[sheet]['data']:
                if repo == repo_name:
                    return application_name_data[sheet]['data'][repo]['placeholders']['#APPLICATION-NAME#']['value']


    def rename_repo(self, repo , location, pattern, new_name):
        error_code = os.system(f'cd {location}; mv {pattern} {new_name};')
        if error_code == 0: 
            self.info(f'successfully renamed built repo "{repo}"', console=True)
        elif error_code == 256:
            self.warn(f'renaming repo skipped for repo "{repo}" as there exists file with same name ' , console=True)
        else: 
            self.error(f'renaming failure for repo "{repo}"', console=True)


    def build_repo(self, repo, build_directory, build_command):
        error_code = os.system(f'cd {build_directory}; {build_command};')
        if error_code == 0:
            self.info(f'successfully built repo "{repo}"', console=True)
        else:
            self.error(f'build failure repo "{repo}"', console=True)


    def run(self):
        for repo in self._data:
            self.info(f'building repo "{repo}"', console=True)
            project_name = self.get_project_name(repo)
            build_path = self._data[repo]['build-path']
            package_path = self._data[repo]['package-path']
            
            build_directory = self._config['dirs']['source-dir'] + '/'+ project_name + '/' + repo + '/' + build_path + '/'
            package_directory = self._config['dirs']['source-dir'] + '/' + project_name + '/' + repo + '/' + package_path
            package_name_pattern = self._data[repo]['package-name']

            build_command = self._data[repo]['build-command']
            application_name = self.get_application_name(repo)

            self.build_repo(repo, build_directory, build_command)
            
            new_package_format = self._data[repo]['new-package-format']
            application_name = "" if application_name == None else application_name

            new_name = f'{application_name}{new_package_format}'
            self.rename_repo(repo, package_directory, package_name_pattern, new_name)












