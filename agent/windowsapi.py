"""
Available calls to Windows. Uses WMI for access.
"""
import logging

import wmi

import core.config
from core.log import logger as log

def doWMI():
    log.debug("doWMI : " + __name__ + " loaded")
    c = wmi.WMI()
    try:
        os = c.OperatingSystem()
        log.info("WMI: " + os[0].CSName)
        return True
    except AttributeError:
        return False
    
