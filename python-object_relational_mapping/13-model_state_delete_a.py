#!/usr/bin/python3
"""
Module that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a():
    """
    Connects to MySQL database, finds all states containing 'a',
    deletes them, and commits the session.
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

    # Query all states containing the letter 'a'
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    delete_states_with_a()
