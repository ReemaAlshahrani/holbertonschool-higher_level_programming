#!/usr/bin/python3
"""
Module that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument,
safe from MySQL injections.
"""

import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to MySQL database and safely prints states
    matching the user argument ordered by states.id.
    """
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
