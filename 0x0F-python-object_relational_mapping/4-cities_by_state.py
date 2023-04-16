#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa:
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities,
                states WHERE cities.state_id = states.id ORDER BY id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
