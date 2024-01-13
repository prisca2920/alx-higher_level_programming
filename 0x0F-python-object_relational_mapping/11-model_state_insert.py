#!/usr/bin/python3
"""the first state obj in the db"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
    )

    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    newstate = State(name="Louisiana")
    session.add(newstate)
    session.commit()

    print("{}".format(newstate.id))
