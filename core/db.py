"""
All database access uses this module except django.
"""
from sqlite3 import dbapi2 as sqlite

import core.config
from core.log import mylogger as log

def start_database():
    """
    This isn't robust. If the file doesn't exist this call just creates it. We neeed to find
    a better way to open to file or check for it's existence.
    maybe something like:
       dbdir = os.path.dirname(path)
       if not os.access(path, os.R_OK + os.W_OK) or
           not os.access(dbdir, os.R_OK + os.W_OK):
    WARNING: need to investiage thread safety
    """
    con = sqlite.connect(core.config.DBFILE)
 
    if con:
        cur = con.cursor()

        # Execute the SELECT statement:
        cur.execute("select * from monrito_systems")

        # Retrieve all rows as a sequence and print that sequence:
        log.debug(cur.fetchall())
        return True
    else:
        return False   
