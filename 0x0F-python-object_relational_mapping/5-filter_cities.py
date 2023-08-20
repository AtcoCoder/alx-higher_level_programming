#!/usr/bin/python3
"""Filters cities by state"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    query = "SELECT cities.name\
            FROM cities\
            JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC;"

    db = MySQLdb.connect(user=username, password=password, database=database)
    cur = db.cursor()
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    length = len(rows)

    for index, row in enumerate(rows):
        if index != length - 1:
            print(row[0], end=', ')
        else:
            print(row[0])

    cur.close()
    db.close()
