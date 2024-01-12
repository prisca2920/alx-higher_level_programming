#!/usr/bin/python3
"""displays all values in the states table """
import sys
import MYSQLdb


if __name__ == '__main__':
    db = MYSQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))

    rows = curs.fetchall()

    for row in rows:
        print(row)
