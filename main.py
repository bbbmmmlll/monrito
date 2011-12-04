"""
Main module for Monrito.

Monrito: Rich Enterprise Monitoring.
    
Start threads.
"""
import sys
import time

import core.config
import core.timer
from core.log import mylogger as log
import core.db
import core.worker

PROGNAME = 'Monrito'
VERSION = '0.0.16'

log.info(PROGNAME + ' version ' + VERSION + ' starting')

log.info('Starting Database: ')
DB = core.db.start_database()
if DB:
    log.info('Database started')
else:
    log.critical('Database failed to initalize - aborting')
    sys.exit(1)

log.info('Starting Timer: ')
TM = core.timer.Timer()
if TM:
    log.info('Timer started')
else:
    log.critical('Timer failed to initalize - aborting')
    sys.exit(1)

# do nothing useful for now                  
while True:
    time.sleep(600)

