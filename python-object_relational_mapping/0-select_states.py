#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

MY_HOST = 'localhost'
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]

if __name__ == '__main__':
    db = MySQLdb.connect(host=MY_HOST, port=3306, user=MY_USER, passwd=MY_PASS, database=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))

    cur.close()
    db.close()
