# TODO: add ability to toggle debug off/on
import logging
import logging.handlers

import core.config

def init_logger():
    """
    Set up log system.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
             
    # console logger
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(module)s[%(levelname)s]: %(message)s')
    console.setFormatter(formatter)
    logger.addHandler(console)
            
    # debug logger
    # TODO: the following is broken, but patched in Python CVS
    #debuglog = logging.handlers.RotatingFileHandler(app.config.DEBUG_LOGFILE, 
    #                                                'a', 1000000, 10)
    debuglog = logging.FileHandler(core.config.DEBUG_LOGFILE)
    debuglog.setLevel(logging.DEBUG)
    formatter = logging.Formatter(core.config.LOG_FORMAT, 
                                  core.config.LOG_TIME_FORMAT)
    debuglog.setFormatter(formatter)
    logger.addHandler(debuglog)
            
    # standard logger
    # BUG: the following is broken, but patched in Python CVS
    #stdlog = logging.handlers.RotatingFileHandler(app.config.DEFAULT_LOGFILE,
    #                                              'a', 1000000, 10)
    stdlog = logging.FileHandler(core.config.DEFAULT_LOGFILE)
    stdlog.setLevel(logging.INFO)
    formatter = logging.Formatter(core.config.LOG_FORMAT,
                                  core.config.LOG_TIME_FORMAT)
    stdlog.setFormatter(formatter)
    logger.addHandler(stdlog)

# initial logging details
init_logger()
mylogger = logging.getLogger()
