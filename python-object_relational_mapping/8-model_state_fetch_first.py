#!/usr/bin/python3
"""
Module that prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state():
    """
    Connects to MySQL database and prints the first State object
    ordered by states.id, or 'Nothing' if the table is empty.
    """
    if len(sys.argv) != 4:
        return

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first state ordered by id using .first() instead of .all()
    state = session.query(State).order_by(State.id).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    fetch_first_state()
