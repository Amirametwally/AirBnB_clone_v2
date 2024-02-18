#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """class for user"""

    __tablename__ = "users"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship(
            "Place", back_populates="user", cascade="all, delete, delete-orphan"
        )
        reviews = relationship(
            "Review", back_populates="user", cascade="all, delete, delete-orphan"
        )
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
