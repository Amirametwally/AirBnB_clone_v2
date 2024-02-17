#!/usr/bin/python3
"""Class state that inherit from Basemodel"""


from models.base_model import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """class State inherits from BaseModel and Base"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
