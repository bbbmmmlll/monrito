"""
Logic for talking to a Windows system.

"""
import logging

import core.config
import core.windowsapi
from core.log import logger as log

def tryWindows():
    log.debug("Trying Windows")
    ret = core.windowsapi.doWMI()
    log.debug("Windows done")
    return ret
    