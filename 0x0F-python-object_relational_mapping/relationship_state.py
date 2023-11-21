#!/usr/bin/python3
"""Contains the def of a state
and an instance Base 
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """inherits from base, links """
    __table__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True,
            primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete',backref='state')
