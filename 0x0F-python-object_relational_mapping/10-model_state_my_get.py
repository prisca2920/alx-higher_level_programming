#!/usr/bin/python3
"""fetching all states"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    """fetching all states via an orm"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name == argv[4]).first()

    if states:
        print(states.id)
    else:
        print('Not found')
