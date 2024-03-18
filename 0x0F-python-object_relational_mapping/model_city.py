#!/usr/bin/python3
"""class definition of a city"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class definition of a city"""

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
