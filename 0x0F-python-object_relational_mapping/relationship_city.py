#!/usr/bin/python3
"""Contains the City class definition"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, String, Column, ForeignKey
from relationship_state import Base, State


class City(Base):
    """inherits from Base model
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State')
