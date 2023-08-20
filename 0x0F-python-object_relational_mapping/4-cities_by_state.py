#!/usr/bin/python3
"""Select States  with name Module"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    query = "SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC;"

    db = MySQLdb.connect(user=username, password=password, database=database)
    cur = db.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
