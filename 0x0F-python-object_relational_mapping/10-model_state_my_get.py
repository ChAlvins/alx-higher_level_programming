#!/usr/bin/python3
"""
 a script that prints the State object with the name passed
 as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys


if __name__ == '__main__':
    args = sys.argv
    username = args[1]
    password = args[2]
    dbname = args[3]
    state_name = args[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dbname))
    # create session
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    states = session.query(State).filter(State.name == state_name)\
                    .order_by(State.id)
    if states is not None and states.count() > 0:
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')
    session.close()
