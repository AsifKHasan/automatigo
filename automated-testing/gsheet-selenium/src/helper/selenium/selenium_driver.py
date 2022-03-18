#!/usr/bin/env python3
'''
'''
import sys
import time
import pprint
import inspect
import traceback

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

from helper.utils import *
from helper.logger import *

class SeleniumDriver(object):

    ''' if any of the activity under any of the processes has a data-key, then this work needs data
    '''
    def this_work_needs_data(self, work_name):
        for process_name, process in self._workflow[work_name].items():
            for activity in process:
                if 'data-key' in activity:
                    return True

        return False


    def drive(self, data):
        self._all_case = data['test-case']
        self._workflow = data['workflow']

        if self._config['test']['case'] in self._all_case:
            self.info('test case {0} found in data'.format(self._config['test']['case']))
            self._case = self._all_case[self._config['test']['case']]
        else:
            self.error('test case {0} not found in data'.format(self._config['test']['case']))
            return self._log

        # hit url, this is the begining of timing
        self._begining = int(round(time.time() * 1000))
        if not self.load(self._case['url']):
            return self._log

        # iterate through all work under the workflow
        self._work_sequence = 0
        self._image_sequence = 0
        for work_name in self._workflow:
            self._current_work = work_name
            self._log[self._current_work] = {}

            # the work may or may not need data
            work_data = None
            if self.this_work_needs_data(work_name):
                # data is needed. if there is a data key in the test-case dictionary with the same name as the wor, that is the data
                if work_name in self._case:
                    debug(f"base data found for work [{work_name}]")
                    work_data = self._case[work_name]

                else:
                    # there may be a function to get data for that work data
                    func_name = '{0}_data'.format(work_name.replace('-', '_'))

                    # check whether the function is implemented, if implemented call it to have the data for the work
                    if is_method(self.__class__, func_name):
                        debug(f"function geneareted data found for work [{work_name}]")
                        work_data = (method_by_name(self.__class__, func_name))(self, self._case)

            # if the data is a dict, we just perform the work once
            if work_data is None or isinstance(work_data, dict):
                if not self.perform_work(work_name, work_data):
                    return self._log

            # if the data we got is a list, we need to perform the work for each element of the list
            elif isinstance(work_data, list):
                index = 1
                for i in range(len(work_data)):
                    if not self.perform_work(work_name, work_data[i], index):
                        return self._log

                    index = index + 1

            # if there is a default delay after the work, delay
            if 'default-seconds' in self._config:
                if 'between-work' in self._config['default-seconds']:
                    time.sleep(float(self._config['default-seconds']['between-work']))

            self._work_sequence = self._work_sequence + 1
            # input("Press Enter to continue...")

        return self._log

    def perform_work(self, work_name, work_data, index=0):
        for process in self._workflow[work_name]:
            self._current_process = process
            if index != 0:
                self._current_process_with_index =  '{0}-{1}'.format(self._current_process, index)
            else:
                self._current_process_with_index = self._current_process

            self._log[self._current_work][self._current_process_with_index] = []

            if not self.perform_process(work_name, self._current_process, work_data):
                self.error('{0} failed'.format(work_name))
                return False

        return True

    def perform_process(self, work_name, process_name, work_data):
        work = self._workflow[work_name][process_name]
        if work is None:
            self.warn('nothing to do for process {0} of {1}'.format(process_name, work_name))
            return True

        # perform activities
        self.info('{0} process starting for {1}'.format(process_name, work_name))
        for activity in work:

            if activity['action'] is None:
                continue

            if 'data-key' in activity and activity['data-key'] in work_data and work_data[activity['data-key']] is None:
                self.warn('skipping action for {0}'.format(work_name))
                continue

            # the xpath may contain a placeholder, handle it
            if 'xpath' in activity:
                if work_data is not None:
                    xpath = activity['xpath'].format(_=work_data)
                else:
                    xpath = activity['xpath']
            else:
                xpath = None

            self.mark_activity_time()
            if activity['action'] in ['entry', 'click', 'hover', 'select', 'check']:

                if 'xpath' in activity:

                    try:
                        wait = WebDriverWait(self._browser, float(self._config['default-seconds']['element-wait']))
                        elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                    except Exception as e:
                        self.error('{0} timeout for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                                   timing=True, activity=activity)
                        traceback.print_exc()
                        return False

                else:
                    self.warn('xpath is required for action {0}'.format(activity['action']), timing=True,
                              activity=activity)
                    continue

                # check we have found anything
                if elements is None or (isinstance(elements, list) and len(elements) == 0):
                    self.error('{0} not found for xpath {1}'.format(activity['action'], activity['xpath']), timing=True,
                               activity=activity)
                    return False

                # element found, perform action
                if isinstance(elements, list):
                    element = elements[0]
                else:
                    element = elements

                # entry
                if activity['action'] == 'entry':
                    try:
                        self.debug('sending keys for entry : {0}'.format(work_data[activity['data-key']]), activity=activity)
                        element.send_keys(work_data[activity['data-key']])
                    except Exception as e:
                        self.error(
                            '{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                            timing=True, activity=activity)
                        traceback.print_exc()
                        return False

                # click
                elif activity['action'] == 'click':
                    try:
                        target = ActionChains(self._browser).move_to_element(element)
                        target.click(element).perform()
                    except Exception as e:
                        self.error(
                            '{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                            timing=True, activity=activity)
                        traceback.print_exc()
                        return False

                # hover
                elif activity['action'] == 'hover':
                    try:
                        hover = ActionChains(self._browser).move_to_element(element)
                        hover.perform()
                    except Exception as e:
                        self.error(
                            '{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                            timing=True, activity=activity)
                        traceback.print_exc()
                        return False

                # select
                elif activity['action'] == 'select':
                    try:
                        # target = ActionChains(self._browser).move_to_element(element)
                        # target.click(element).perform()
                        element.click()
                    except Exception as e:
                        self.error(
                            '{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                            timing=True, activity=activity)
                        traceback.print_exc()
                        return False

                # check
                elif activity['action'] == 'check':
                    try:
                        # target = ActionChains(self._browser).move_to_element(element)
                        # target.click(element).perform()
                        if work_data[activity['data-key']] == 'TRUE':
                            element.click()
                        else:
                            continue
                    except Exception as e:
                        self.error(
                            '{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                            timing=True, activity=activity)
                        traceback.print_exc()
                        return False

            # wait-presence
            elif activity['action'] == 'wait-presence':
                try:
                    wait = WebDriverWait(self._browser, float(self._config['default-seconds']['element-wait']))
                    elements = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
                except Exception as e:
                    self.error('{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                               timing=True, activity=activity)
                    traceback.print_exc()
                    return False

            # wait-visible
            elif activity['action'] == 'wait-visible':
                try:
                    wait = WebDriverWait(self._browser, float(self._config['default-seconds']['element-wait']))
                    elements = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                except Exception as e:
                    self.error('{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                               timing=True, activity=activity)
                    traceback.print_exc()
                    return False

            # wait-clickable
            elif activity['action'] == 'wait-clickable':
                try:
                    wait = WebDriverWait(self._browser, float(self._config['default-seconds']['element-wait']))
                    elements = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                except Exception as e:
                    self.error('{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                               timing=True, activity=activity)
                    traceback.print_exc()
                    return False

            # wait-selectable
            elif activity['action'] == 'wait-selectable':
                try:
                    wait = WebDriverWait(self._browser, float(self._config['default-seconds']['element-wait']))
                    elements = wait.until(EC.element_to_be_selected((By.XPATH, xpath)))
                except Exception as e:
                    self.error('{0} failed for xpath {1} : {2}'.format(activity['action'], xpath, str(e)),
                               timing=True, activity=activity)
                    traceback.print_exc()
                    return False

            # screen-shot
            elif activity['action'] == 'screen-shot':
                file_path = '{0}/{1}-{2}__{3}.png'.format(self._config['dirs']['temp-dir'],
                                                          str(self._work_sequence).zfill(2),
                                                          str(self._image_sequence).zfill(3), activity['image'])
                self._browser.get_screenshot_as_file(file_path)
                self.debug('{0} taken at {1}'.format(activity['action'], file_path), timing=True, activity=activity)
                self._image_sequence = self._image_sequence + 1
                continue

            # delay
            elif activity['action'] == 'delay':
                time.sleep(float(activity['seconds']))
                self.debug('{0} performed for {1} seconds'.format(activity['action'], float(activity['seconds'])),
                           timing=True, activity=activity)
                continue

            else:
                self.warn('action {0} not supported yet'.format(activity['action']), timing=True, activity=activity)
                continue

            self.debug('{0} passed for xpath {1}'.format(activity['action'], xpath), timing=True,
                       activity=activity)

        self.info('{0} check passed for {1}'.format(process_name, work_name))
        return True

    def mark_activity_time(self):
        self._last_mark = int(round(time.time() * 1000))

    def debug(self, msg, timing=False, activity=None, console=False):
        self.log('debug', msg, timing, activity, console)

    def info(self, msg, timing=False, activity=None, console=False):
        self.log('info', msg, timing, activity, console)

    def warn(self, msg, timing=False, activity=None, console=False):
        self.log('warn', msg, timing, activity, console)

    def error(self, msg, timing=False, activity=None, console=False):
        self.log('error', msg, timing, activity, console)

    def log(self, level, msg, timing=False, activity=None, console=False):
        data = {'type': level, 'time': datetime.now().isoformat(), 'msg': msg}
        if activity:
            data['activity'] = activity

        if timing:
            now = int(round(time.time() * 1000))
            data['elapsed'] = now - self._begining
            data['this-activity'] = now - self._last_mark

        if self._current_process:
            self._log[self._current_work][self._current_process_with_index].append(data)
        else:
            self._log[self._current_work].append(data)

        if console:
            print('{0} {1:<6} {2}'.format(data['time'], data['type'], data['msg']))

    def __init__(self, config):
        self._config = config
        self._log = {}
        self._current_work = '-'
        self._log[self._current_work] = []
        self._current_process = None
        self.start_time = int(round(time.time() * 1000))

    def __del__(self):
        if self._browser:
            self._browser.close()

        self.end_time = int(round(time.time() * 1000))
        info("Selenium took {} seconds".format((self.end_time - self.start_time) / 1000))

    def load(self, url):
        if self._config['driver'] == 'firefox':
            if self._config['platform'] == 'Windows':
                binary = self._config['firefox-path']
                self._browser = webdriver.Firefox(firefox_binary=binary, executable_path='../drivers/geckodriver.exe')
            else:
                self._browser = webdriver.Firefox()

        elif self._config['driver'] == 'edge':
            self._browser = webdriver.Edge(executable_path='../drivers/MicrosoftWebDriver.exe')

        elif self._config['driver'] == 'ie':
            self._browser = webdriver.Ie(executable_path='../drivers/IEDriverServer.exe')

        else:
            if self._config['platform'] == 'Windows':
                self._browser = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
            else:
                self._browser = webdriver.Chrome()

        self._browser.maximize_window()
        self._browser.implicitly_wait(0)

        try:
            self.info('loading {0}'.format(url))
            self.mark_activity_time()
            self._browser.get(url)
            self.info('loaded {0}'.format(url), timing=True)
            return True
        except Exception as e:
            self.error('load failed {0}'.format(url), timing=True)
            self.error(str(e))
            return False
