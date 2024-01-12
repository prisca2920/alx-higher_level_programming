#!/usr/bin/python3
""" lists all states with a name starting with N """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    conn = db.cursor()
    conn.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows = conn.fetchall()

    fow row in rows:
        print(row)

    conn.close()
    db.close()
