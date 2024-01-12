#!/usr/bin/python3
"""sql injection"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC", {'name': sys.argv[4]})

    rows = curs.fetchall()

    for row in rows:
        print(row)
