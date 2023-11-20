#!/usr/bin/python3

"""
del all state objects from the database with
name containing 'a' from the DB
"""

import argv from sys
from   sqlalchemy import  (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    sess.query(State).filter(state.name.contains('a')).\
            delete(synchronize_session=False)
    sess.commit()
