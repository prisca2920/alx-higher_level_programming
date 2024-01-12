#!/usr/bin/python3
"""displays all values in the states table """
import sys
import MYSQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MYSQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))

    rows = curs.fetchall()

    for row in rows:
        print(row)
