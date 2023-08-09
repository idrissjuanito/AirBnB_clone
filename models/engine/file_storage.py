#!/usr/bin/env python3
""" Module holds classes for managing data storage """
import json
from os import path


class FileStorage():
    """
        handles serialization and deserialization of object
        dictionaries to json and saves them to file
        Attributes:
            file_path (str): path of the file for saving object data
            objects (dict): dictionary record of all objects in storage
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
                obj (dict): the the new object to store
        """
        FileStorage.__objects[obj['__class__']+"."+obj['id']] = obj

    def save(self):
        """ Method writes all objects data into a json file"""
        with open(FileStorage.__file_path, 'w') as fl:
            json.dump(FileStorage.__objects, fl)

    def reload(self):
        """
            Loads and reads stored data from a json file
            and stores into objects dictionaty
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fl:
                FileStorage.__objects = json.load(fl)
