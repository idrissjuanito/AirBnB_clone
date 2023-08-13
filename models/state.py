#!/usr/bin/python3
""" State module for managing states """
from models.base_model import BaseModel


class State(BaseModel):
    """
        State class for creating new state objects
        Attributes:
            name (str): name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super(State, self).__init__(**kwargs)
        else:
            super(State, self).__init__()
