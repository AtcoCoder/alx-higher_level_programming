#!/usr/bin/python3
"""Sript that prints the first State objects from the database hbtn_0e_6_usa
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

    state = session.query(State).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
