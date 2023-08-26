#!/usr/bin/python3
"""Contains the State class definition"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class State(Base):
    """inherits from Base model
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
