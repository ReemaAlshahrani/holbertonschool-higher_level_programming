#!/usr/bin/python3
"""
Module that defines the State class and Base instance
using SQLAlchemy for object-relational mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that links to the MySQL table 'states'.

    Attributes:
        __tablename__ (str): The name of the table in MySQL.
        id (int): The state's unique identifier (Primary Key).
        name (str): The state's name (up to 128 characters).
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
