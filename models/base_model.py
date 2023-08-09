#!/usr/bin/python3
"""Base Model module"""
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """
    defines all base attributes to used by other classes of the program
    id (string): uniq identifier of object
    created_at (datetime): records time an object was created
    updated_at (datetime): records the current time with each change of the object
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k in kwargs.keys():
                if k != "__class__":
                    if k == "created_at" or k == "updated_at":
                        self.__setattr__(k, datetime.fromisoformat(kwargs[k]))
                    else:
                        self.__setattr__(k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the update_at attribute with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Creates a dictionary representation of the object"""
        dct = dict(self.__dict__)
        dct["__class__"] = self.__class__.__name__
        dct["updated_at"] = self.updated_at.isoformat()
        dct["created_at"] = self.created_at.isoformat()
        return dct
