#!/usr/bin/env python3
'''
'''
import os
import sys
import time
import shutil
import traceback
from datetime import datetime
from progress.bar import Bar
# from tqdm import tqdm

from git import Repo
from git import RemoteProgress

from worker.base_worker import BaseWorker

class ProgressPrinter(RemoteProgress):

    _bar = Bar('cloning     ', fill='#', suffix='%(percent).1f%%')
    # _bar = tqdm(desc='cloning     ', bar_format='l_bar', fill = '#', suffix = '%(percent).1f%%')

    def update(self, op_code, cur_count, max_count=None, message=''):
        self._bar.index = cur_count or 0.0
        self._bar.max = max_count or 100.00
        #print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")
        if op_code in [4, 8, 16, 32, 64]:
            if op_code == 4: self._bar.message =  'counting    '
            elif op_code == 8: self._bar.message =  'compressing '
            elif op_code == 16: self._bar.message = 'writing     '
            elif op_code == 32: self._bar.message = 'receiving   '
            elif op_code == 64: self._bar.message = 'resolving   '
            self._bar.update()

class GitRepoWorker(BaseWorker):

    def perform_work(self, data):
        self._data = data['git-repo']['configuration']

        # create directory
        self._src_path = self._config['dirs']['source-dir']
        if not os.path.exists(self._src_path):
            os.makedirs(self._src_path)
        else:
            self.warn('directory : {0} exists. Some repos may alreday be checked out'.format(self._src_path), console=True)

        # work on projects from the inner dict
        for project_name in self._data:
            if not self.process_project(project_name, self._data[project_name]):
                return False, self._log

        return True, self._log

    def process_project(self, project_name, project_data):
        self.info('project : {0} ....'.format(project_name), context_0=project_name, console=True)
        time_1 = time.time()

        # create directory
        self._project_path = '{0}/{1}'.format(self._src_path, project_name)
        if not os.path.exists(self._project_path):
            os.makedirs(self._project_path)

        # process repos from the inner dict
        for repo_name in project_data:
            if not self.process_repo(project_name, repo_name, project_data[repo_name]):
                return False

        self.info('project : {0} done'.format(project_name), context_0=project_name, time_1=time_1, console=True)
        return True

    def process_repo(self, project_name, repo_name, repo_data):
        self.info('repo : {0} ....'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
        time_1 = time.time()

        # password
        if 'USERNAME' not in os.environ:
            self.error('environment variable USERNAME not found', console=True)
            return False

        # password
        if 'PASSWD' not in os.environ:
            self.error('environment variable PASSWD not found', console=True)
            return False

        repo_url = repo_data['url-pattern'].format(username=os.environ['USERNAME'], passwd=os.environ['PASSWD'], repo_name=repo_name)

        # create directory
        path = '{0}/{1}'.format(self._project_path, repo_name)
        if not os.path.exists(path):
            os.makedirs(path)

            # the diretory is not a git repo, clone
            self.clone_repo(project_name, repo_name, repo_data, path, repo_url)

        else:
            # check if the directory has this specific repo checked in
            repo = self.repo_at_path(project_name, repo_name, repo_data, path)
            if repo:
                # it is a git working dir, check if it is the correct one
                if repo.remote("origin").url != repo_url:
                    # not the correct working tree for repo
                    self.error('path : {0} is not working tree for repo: {1}'.format(path, repo_name), context_0=project_name, context_1=repo_name, console=True)

                else:
                    # it is the correct working tree for repo, check if it is the same branch
                    if repo.active_branch.name == repo_data['branch']:
                        # it is the same branch, pull if necessary
                        self.debug('repo : {0} working tree branch is {1}, same as specified branch {2}'.format(repo_name, repo.active_branch.name, repo_data['branch']), context_0=project_name, context_1=repo_name, console=True)
                        self.pull_repo(repo, project_name, repo_name, repo_data)

                    else:
                        # it is not the same branch, branch
                        self.warn('repo : {0} working tree branch is {1} which is different from specified branch {2}'.format(repo_name, repo.active_branch.name, repo_data['branch']), context_0=project_name, context_1=repo_name, console=True)

                        # branch out
                        if self.checkout_branch(repo, repo_data['branch'], project_name, repo_name):
                            self.pull_repo(repo, project_name, repo_name, repo_data)

            else:
                # it is not a git working dir, clean and clone
                try:
                    self.info('cleaning path : {0}'.format(path), context_0=project_name, context_1=repo_name, console=True)
                    shutil.rmtree(path)
                    cleaned = True
                except Exception as e:
                    cleaned = False
                    self.error('path : {0} could not be cleaned, repo {1} could not be processed'.format(path, repo_name), context_0=project_name, context_1=repo_name, console=True)

                if cleaned:
                    self.clone_repo(project_name, repo_name, repo_data, path, repo_url)

        self.info('repo : {0} done'.format(repo_name), context_0=project_name, context_1=repo_name, time_1=time_1, console=True)

        return True

    def clone_repo(self, project_name, repo_name, repo_data, path, repo_url):
        self.debug('repo : {0} is not checked out, cloning'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
        try:
            git_repo = Repo.clone_from(repo_url, path, branch=repo_data['branch'], progress=ProgressPrinter())
            self.debug('repo : {0} cloned'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
        except Exception as e:
            self.error(str(e), context_0=project_name, context_1=repo_name, console=True)
            self.error(traceback.format_exc(), context_0=project_name, context_1=repo_name, console=True)
            self.error('repo : {0} cloning failed'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
            traceback.print_exc()

    def repo_at_path(self, project_name, repo_name, repo_data, path):
        try:
            repo = Repo(path, search_parent_directories=False)
            return repo
        except Exception as e:
            self.info('path : {0} is not a valid git working dir'.format(path), context_0=project_name, context_1=repo_name, console=True)
            traceback.print_exc()
            return None

    def pull_repo(self, repo, project_name, repo_name, repo_data):
        self.debug('repo : {0} may not be current, pulling'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
        try:
            o = repo.remotes.origin
            o.pull(progress=ProgressPrinter())
            self.debug('repo : {0} pull successful'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
        except Exception as e:
            self.error(str(e), context_0=project_name, context_1=repo_name, console=True)
            self.error(traceback.format_exc(), context_0=project_name, context_1=repo_name, console=True)
            self.debug('repo : {0} pull failed'.format(repo_name), context_0=project_name, context_1=repo_name, console=True)
            traceback.print_exc()

    def checkout_branch(self, repo, branch, project_name, repo_name):
        self.debug('repo : {0} checking out branch {1}'.format(repo_name, branch), context_0=project_name, context_1=repo_name, console=True)
        try:
            pass
        except Exception as e:
            self.error(str(e), context_0=project_name, context_1=repo_name, console=True)
            self.error(traceback.format_exc(), context_0=project_name, context_1=repo_name, console=True)
            self.debug('repo : {0} checkout to branch {1} failed'.format(repo_name, branch), context_0=project_name, context_1=repo_name, console=True)
            traceback.print_exc()
