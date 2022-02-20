#!/usr/bin/env python3
'''
'''
from rsmq.consumer import RedisSMQConsumer

from worker.base_worker import BaseWorker

class MqLogListener(BaseWorker):

    def start(self):
        self.info('worker: {0} starting ...'.format(self._worker_label), time_0=self._start_time, console=True)

        if self.create_consumer():
            super().start()
        else:
            self.error('worker: {0} start failed ...'.format(self._worker_label), time_0=self._start_time, console=True)

        return self._is_running

    def stop(self):
        self.info('worker: {0} stopping ...'.format(self._worker_label), time_0=self._start_time, console=True)

        super().stop()

    def create_consumer(self):
        # create consumer
        self._consumer = RedisSMQConsumer(self._worker_config['args']['queue-name'], self.processor, host=self._worker_config['args']['host'], port=self._worker_config['args']['port'])

        # run consumer
        self._consumer.run()

    def processor(self, id, message, rc, ts):
        print('message received')
        print('{0} : {1}'.format(id, message))

        # ask all dependent workers to process the message
        for processor in self._worker_config['processors']:
            if processor in self._global_context['active-workers']:
                self._global_context['active-workers'][processor].process(message)

        print('waiting for message ....')

        return True
