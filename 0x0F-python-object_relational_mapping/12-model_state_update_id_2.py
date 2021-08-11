#!/usr/bin/python3
"""changes the name of a State from database
"""
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
    fetch_objects = session.query(State).get(2)
    fetch_objects.name = "New Mexico"
    session.commit()
