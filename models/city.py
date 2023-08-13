#!/usr/bin/python3
""" City module for managing cities """
from models.base_model import BaseModel


class City(BaseModel):
    """
        City class for creating new city objects
        Attributes:
            name (str): name of the City
            state_id (str): state wheere city in
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super(City, self).__init__(**kwargs)
        else:
            super(City, self).__init__()
