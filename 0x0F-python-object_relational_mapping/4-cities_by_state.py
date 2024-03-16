#!/usr/bin/python3
"""lists cities by states"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """connects to mysql db"""
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
