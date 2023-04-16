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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, dbname))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State()
    new_state.name = 'Lousiana'
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
