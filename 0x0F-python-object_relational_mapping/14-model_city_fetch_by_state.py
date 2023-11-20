#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sys import argv

    if (len(argv) != 4):
        print('Use: username, password database_name')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(
        City,
        State).filter(
        State.id == City.state_id).order_by(
            City.id)
    for (city, state) in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
