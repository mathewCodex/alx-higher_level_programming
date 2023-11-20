#!/usr/bin/python3

"""
contains the clas  defineition of a city
"""

from sqlalchemy importColumn, Integer, String,  ForeignKey
from model_state import Base


class City(Base):
    """
    Representation of the table cities
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
