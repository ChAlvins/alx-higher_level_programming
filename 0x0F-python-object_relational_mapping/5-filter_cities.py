#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    state_name = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbname, port=3306)
    cur = db.cursor()
    query = """
            SELECT cities.name FROM states
                INNER JOIN cities
                    ON states.id = cities.state_id
                    WHERE states.name = %s
                ORDER BY cities.id ASC;
            """
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
