#!/usr/bin/python3
"""
 script that deletes all State objects with a name
 containing the letter a from the database
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dbname))
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
