#!/usr/bin/python3
"""class FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects the obj"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionary_obj = {}
        for key, val in FileStorage.__objects.items():
            dictionary_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary_obj, file)

    def delete(self, obj):
        """Delete obj from __objects if it’s inside"""
        key = obj.__class__.__name__ + "." + obj.id
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]

    def get(self, cls, id):
        """Return an object based on the class name and its ID,
        or None if not found"""
        key = cls + "." + id
        return FileStorage.__objects.get(key, None)

    def reload(self):
        """deserialize the JSON file to __object"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
                for key, val in FileStorage.__objects.items():
                    if val["__class__"] == "User":
                        FileStorage.__objects[key] = User(**val)
                    elif val["__class__"] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**val)
                    elif val["__class__"] == "Place":
                        FileStorage.__objects[key] = Place(**val)
                    elif val["__class__"] == "State":
                        FileStorage.__objects[key] = State(**val)
                    elif val["__class__"] == "City":
                        FileStorage.__objects[key] = City(**val)
                    elif val["__class__"] == "Amenity":
                        FileStorage.__objects[key] = Amenity(**val)
                    elif val["__class__"] == "Review":
                        FileStorage.__objects[key] = Review(**val)
        except FileNotFoundError:
            pass
