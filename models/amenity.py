#!/usr/bin/python3
""" Amenity module for managing amenities """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
        Amenity class for creating new Amenity objects
        Attributes:
            name (str): name of the Amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super(Amenity, self).__init__(**kwargs)
        else:
            super(Amenity, self).__init__()
