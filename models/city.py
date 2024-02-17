#!/usr/bin/python3
"""class city that inherit from BaseModel"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """class city inherits from BaseModel and Base"""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship("State", backref="cities")
