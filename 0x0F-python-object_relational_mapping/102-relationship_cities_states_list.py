#!/usr/bin/python3
"""Create State California with the City San Francisco from the database
hbtn_0e_100_usa"""
from relationship_city import City
from relationship_state import State, Base
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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
