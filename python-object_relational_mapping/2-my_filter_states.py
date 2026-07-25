#!/usr/bin/python3
"""
Module that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, using MySQLdb.
"""

import MySQLdb
import sys


def filter_states_by_name():
    """
    Connects to MySQL database and prints states matching the user argument
    ordered by states.id in ascending order.
    """
    if len(sys.argv) != 5:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute SQL query using format with user input
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        state_name
    )
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name()
