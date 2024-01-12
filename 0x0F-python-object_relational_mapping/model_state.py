#!/usr/bin/python3
"""the class definition of a state"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """defining class state"""
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False,
            unique=True)
    name = Column(String(128), nullable=False)
