#!/usr/bin/python3
"""contains class difinition of city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base, State


class City(Base):
    """inherits from Base"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
