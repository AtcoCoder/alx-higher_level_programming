#!/usr/bin/python3
"""Select States  with name Module"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE states.name='{}' ORDER BY states.id ASC;"

    db = MySQLdb.connect(user=username, password=password, database=database)
    cur = db.cursor()
    cur.execute(query.format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
