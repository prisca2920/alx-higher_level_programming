#!/usr/bin/python3
"""lists cities by states"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """connects to mysql db"""
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s\
            ORDER BY cities.id ASC", {'state_name': argv[4]})

    rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
