#!/usr/bin/python3
"""Create State 'California' with the City 'San Francisco' from the database
hbtn_0e_100_usa"""
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy.orm import declarative_base

user = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == '__main__':
    db_url = "mysql+mysqldb://{}:{}@localhost/{}"

    engine = create_engine(db_url.format(user, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State()
    state.name = "California"
    print(state.name)
    session.add(state)
    session.commit()
    city = City(name="San Francisco", state_id=state.id)
    session.add(city)
    session.commit()
    session.close()
