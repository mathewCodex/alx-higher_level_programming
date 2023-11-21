#!/usr/bin/python3
"""
List all state objects fron DB hbtn***
"""

if __name__ = "__main__":
    from sqlalchemy.orm import  sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    if (len(argv) != 4):
        print('Use: username, password, database_name')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3], pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        states = session.query(state).order_by(state.id).all()

        for row in states:
            print("{}: {}".format(state.id, state.name))

        session.close()
