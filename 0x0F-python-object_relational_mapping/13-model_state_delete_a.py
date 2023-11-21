#!/usr/bin/python3

"""
del all state objects from the database with
name containing 'a' from the DB
"""

import argv from sys
from sqlalchemy import  (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.ilike('%a%')).all()


    for state in states:
        session.delete(state)

    session.commit()

    session.close()
