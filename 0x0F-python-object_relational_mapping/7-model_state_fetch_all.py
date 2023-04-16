#!/usr/bin/python3
"""
 lists all State objects from the database hbtn_0e_6_usa
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
    # create session from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()
