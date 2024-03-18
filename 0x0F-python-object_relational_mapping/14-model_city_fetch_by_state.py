#!/usr/bin/python3
"""fetching all states"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_city import City


if __name__ == '__main__':
    """fetching all states via an orm"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(
            city.state.name, city.id, city.name))
