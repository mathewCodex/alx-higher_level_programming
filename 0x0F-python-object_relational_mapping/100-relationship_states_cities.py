#!/usr/bin/python3
"""
Creates the state "California" with city "san Francisco" fro DB
"""
from sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name = "California")
    new_city = City(name = "San Francisco", state=new_state)
    new_state.cities.append(new_city)
    session.add(new_state)
    session.add(new_city)
    session.commit()
