"""
Main collector module.

Monrito: Rich Enterprise Monitoring.
    
"""

import threading

import core.config
from core.log import mylogger as log

class Collector(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName('Collector')
        self.start()
        
def run(self):
        nop
