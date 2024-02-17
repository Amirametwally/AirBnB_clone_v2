#!/usr/bin/python3

"""class city that inherit from BaseModel"""
import models
from models.place import Place
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv


type_of_storage = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """class city inherits from BaseModel and Base"""

    __tablename__ = "cities"
    if type_of_storage == "db":
        state_id = Column(
            String(60),
            ForeignKey("states.id"),
            nullable=False,
        )
        name = Column(
            String(128),
            nullable=False,
        )
        places = relationship(
            "Place",
            backref="cities",
            cascade="all, delete-orphan",
        )
    else:
        state_id = ""
        name = ""

        @property
        def places(self):
            """
            Returns the list of Place instances with city_id equals
            to the current City.id
            """
            places = models.storage.all(Place)
            places_lista = []
            for place in places.values():
                if place.city_id == self.id:
                    places_lista.append(place)
            return places_lista
