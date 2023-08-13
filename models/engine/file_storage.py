#!/usr/bin/python3
""" Module holds classes for managing data storage """
import json
from os import path
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }


class FileStorage():
    """
        handles serialization and deserialization of object
        dictionaries to json and saves them to file
        Attributes:
            file_path (str): path of the file for saving object data
            objects (dict): private dictionary record of all objects in storage
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
            gives access to the objects attribute
            which holds all data stored by the app
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Method stores a newly created object into
            the objects dictionary
            Params:
                obj (BaseModel): the the new object to store
        """
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        """ Method writes all objects data into a json file"""
        with open(FileStorage.__file_path, 'w') as fl:
            serializable = {}
            for key, val in FileStorage.__objects.items():
                serializable[key] = val.to_dict()
            json.dump(serializable, fl)

    def reload(self):
        """
            Loads and reads stored data from a json file
            and stores into objects dictionaty
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fl:
                temp_objects = json.load(fl)
                for key, value in temp_objects.items():
                    cls = classes[key.split(".")[0]]
                    FileStorage.__objects[key] = cls(**value)
