"""
OBSOLETE
Task Class

Defines the Task object. Tasks live in Queues.

"""
import time

from core.log import mylogger as log

_TASK_NAMES = ['TASK_TEST', 'TASK_TEST2', 'TASK_FULL_SUBNET_SCAN']

class Task(object):
    """
    Scheduler object.
    """
    def __init__(self, task_name):
        if task_name in _TASK_NAMES:
            self.task_name = task_name
            log.debug('Task created: ' + task_name)
        else:
            self.task_name = 'UNKNOWN'
            log.debug('Task created: ' + task_name)
        self.is_subtask = False
        self.subtask_count = 0
        self.created = time.time()
        self.last_update = self.created
        
    def run_task(self):
        """
        Run current task.
        """
        pass
    
    def next_queue(self):
        """
        TBD
        """
        pass
    
    def self_destruct(self):
        """
        Delete task.
        """
        pass
    
    
