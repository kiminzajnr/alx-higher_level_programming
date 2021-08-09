#!/usr/bin/python3
""" prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""
import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

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
    flag = False
    for state in session.query(State).filter(State.name == sys.argv[4]):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            flag = True
    if flag is False:
        print("Not found")
    session.close()
