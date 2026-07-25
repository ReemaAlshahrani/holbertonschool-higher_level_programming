#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
Connects to a MySQL server running on localhost at port 3306 using MySQLdb.
"""

import MySQLdb
import sys


def list_states():
    """
    Connects to MySQL database and prints all states
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

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select all states ordered by id asc
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
