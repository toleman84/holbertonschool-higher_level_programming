#!/usr/bin/python3
"""SQL Injection..."""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name='{}' \
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
