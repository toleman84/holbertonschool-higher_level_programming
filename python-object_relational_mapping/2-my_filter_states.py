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
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' \
                ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()

    if rows is None:
        cur.close()
        db.close()

    for row in rows:
        print("{}".format(row))

    cur.close()
    db.close()
