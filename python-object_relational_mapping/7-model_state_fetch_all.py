#!/usr/bin/python3
"""
Module that lists all State objects from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_all_states():
    """
    Connects to MySQL database and prints all State objects
    ordered by states.id in ascending order.
    """
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine for MySQL connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()


if __name__ == "__main__":
    fetch_all_states()
