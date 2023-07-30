#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE BINARY states.name='{}' \
                ORDER BY cities.id ASC""".format(sys.argv[4]))
    rows = cur.fetchall()

    count = 0
    for row in rows:
        print("".join(row), end="")
        count += 1
        if count < len(rows):
            print(", ", end="")

    cur.close()
    db.close()
