#!/usr/bin/python3
"""Select States  with like Module"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_like = 'N%'

    db = MySQLdb.connect(user=username, password=password, database=database)
    cur = db.cursor()
    cur.execute(
            """SELECT * FROM states ORDER BY states.id;
            """)

    rows = cur.fetchall()

    for row in rows:
        if row[1].startswith("N"):
            print(row)
