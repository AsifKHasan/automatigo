#!/usr/bin/env python3
'''
'''
import os
import sys
import time
import json
import shutil
import traceback
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import graphviz

from worker.base_worker import BaseWorker

_force_all_stakeholders = True
_force_all_virtual_machines = True
_force_all_docker_containers = True

_deployment_diagram_template = 'grp-deployment-template.gv'
_deployment_diagram_output = 'grp-deployment-diagram'

class NotificationWorker(BaseWorker):

    def perform_work(self, data):

        self._data = data

        # first thing we do is we generate a deployment diagram through GraphViz, it may fail, we ignore failure
        self.generate_deployment_diagram()

        return True, self._log

    def generate_deployment_diagram(self):
        # we do this through a .dot template for diagram which has Jinja templating blocks, so we need data the way the template wants it stakeholder -> vistual-machine -> docker-container
        data_for_template = self.deployment_diagram_data()

        # save data json
        with open('{0}/{1}.json'.format(self._config['dirs']['image-dir'], _deployment_diagram_output), 'w', encoding='utf-8') as f:
            f.write(json.dumps(data_for_template, sort_keys=False, indent=4, ensure_ascii=False))

        env = Environment(loader=FileSystemLoader(self._config['dirs']['template-dir']), extensions=['jinja2.ext.do'])
        template = env.get_template(_deployment_diagram_template)
        deployment_diagram_output = template.render(d=data_for_template)

        # save dot file
        dot_file_path = '{0}/{1}.gv'.format(self._config['dirs']['image-dir'], _deployment_diagram_output)
        with open(dot_file_path, 'w') as f:
            print(deployment_diagram_output, file=f)

        # generate image from dot file
        graphviz.render(engine='dot', format='png', filepath=dot_file_path, renderer=None, formatter=None, quiet=False)

    def deployment_diagram_data(self):
        data_for_template = {}
        for stakeholder, stakeholder_data in self._data['stakeholder']['configuration'].items():
            if not _force_all_stakeholders and stakeholder_data['deploy'] != 'Yes':
                continue

            # valid stakeholder
            data_for_template[stakeholder] = {}

            # now for the virtual machines for the stakeholder, first we check for the existence of the stakeholder
            if stakeholder not in self._data['virtual-machine']['configuration']:
                continue

            # virtual-machines are grouped under vm-type
            for vm_type, vm_type_data in self._data['virtual-machine']['configuration'][stakeholder].items():
                data_for_template[stakeholder][vm_type] = {}

                # now for the virtual-machines under the group
                for host_name, host_data in vm_type_data.items():
                    data_for_template[stakeholder][vm_type][host_name] = host_data
                    data_for_template[stakeholder][vm_type][host_name]['docker-containers'] = {}

                    # docker-container configuration data contains the dictionary of docker-containers under this host_name
                    if stakeholder not in self._data['docker-container']['configuration']:
                        continue

                    if host_name not in self._data['docker-container']['configuration'][stakeholder]:
                        continue

                    # attach the docker-containers to the host
                    data_for_template[stakeholder][vm_type][host_name]['docker-containers'] = self._data['docker-container']['configuration'][stakeholder][host_name]

        return data_for_template
