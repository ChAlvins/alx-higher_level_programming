#!/usr/bin/python3
"""
  a script that changes the name of a State object from the database
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
    new_state = session.query(State).filter(State.id == 2).one()
    new_state.name = 'New Mexico'
    session.commit()
    session.close()
