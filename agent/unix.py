"""
Logic for talking to a UNIX system.
"""
import logging

import core.config
import core.sshclient
from core.log import logger as log

def tryUNIX():
    log.debug("Trying UNIX")
    core.sshclient.doSSH()
    log.debug("UNIX done")
