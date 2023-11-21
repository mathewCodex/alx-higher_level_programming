#!/usr/bin/python3
"""
Creates the state "California" with city "san Francisco" fro DB
"""
from sys import argv
from relationship_state import Base, State
from sqlalchemy import create_engine
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(argv[1], argv[2], argv[3]),
                            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')

    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
