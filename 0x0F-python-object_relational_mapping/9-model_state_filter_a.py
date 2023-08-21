#!/usr/bin/python3
"""Sript that lists all State objects that contain
   the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sqlalchemy
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db_url = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(
                db_url.format(user, password, database),
                pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
