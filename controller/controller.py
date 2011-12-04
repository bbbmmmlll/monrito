"""
Main controller module.

Monrito: Rich Enterprise Monitoring.
    
"""

import threading

import core.config
from core.log import mylogger as log

class Contoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.setName('Controller')
        self.start()
        
def run(self):
        nop
