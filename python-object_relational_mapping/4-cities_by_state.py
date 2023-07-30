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
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                INNER JOIN cities \
                ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))

    cur.close()
    db.close()
