#!/usr/bin/python3
"""This is the review class"""
import os
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """This is the class for Review"""

    __tablename__ = "reviews"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        user = relationship("User", back_populates="reviews")
        place = relationship("Place", back_populates="reviews")

    else:
        text = ""
        place_id = ""
        user_id = ""
