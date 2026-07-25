#!/usr/bin/python3
"""
Module that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa using MySQLdb.
"""

import MySQLdb
import sys


def filter_states():
    """
    Connects to MySQL database and prints states starting with 'N'
    ordered by states.id in ascending order.
    """
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query with BINARY to make it case-sensitive for 'N'
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    )

    # Fetch all rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states()
