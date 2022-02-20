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

class DockerContainerWorker(BaseWorker):

    def perform_work(self, data):
        self._data = data['docker-container']['configuration']
        for stakeholder in self._data:
            for host_vm in self._data[stakeholder]:
                for container_name in self._data[stakeholder][host_vm]:
                    if self._data[stakeholder][host_vm][container_name]['deploy'] != 'Yes':
                        continue

                    docker_file_content=self._data[stakeholder][host_vm][container_name]['dockerfile']
                    docker_build_command=self._data[stakeholder][host_vm][container_name]['docker-build-command']
                    docker_run_command=self._data[stakeholder][host_vm][container_name]['docker-run-command']

                    # authentication = f'ssh -o StrictHostKeyChecking=no -tty -i {self.keypair_path} {self.server_username}@{self.vms_by_id[vm_id][0]["ip"]}'

                    # os.system(f'{authentication} "rm -rf ~/{self.git_username}-Deploy"')
                    self.info(f"Deploying Container {container_name} on {host_vm}")
                    with open("Dockerfile", "w+") as dockerfile:
                        dockerfile.write(docker_file_content)
                        dockerfile.close()
                        # os.system("send_dockerfile_command")
                        os.system(f"docker rm -f {container_name} && docker rmi -f {container_name}-image")
                        os.system(f'{docker_build_command} && {docker_run_command}')
                        os.remove("Dockerfile")

        return True, self._log
