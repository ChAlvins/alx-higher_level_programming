#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    name = args[3]
    statename = args[4]
    # Initializing the DB
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=name, port=3306)
    # Getting the cursor
    cur = db.cursor()
    # Executing the msql statement and exit from db
    num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY
                           '{}' ORDER BY states.id ASC".format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
