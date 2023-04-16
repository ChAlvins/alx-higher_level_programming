#!/usr/bin/python3
"""
a script  prints all City objects from the database
"""
from model_state import Base, State
from model_city import City
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
    # create custom session
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    results = session.query(State.name, City.id, City.name)\
                     .join(City, City.state_id == State.id)\
                     .order_by(City.id)
    for result in results:
        print("{}: ({}) {}".format(result[0], result[1], result[2]))
    session.close()
