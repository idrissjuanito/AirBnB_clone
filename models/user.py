#!/usr/bin/python3
""" User module for managing users """
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class for creating users
        Attributes:
            email (str): user's email
            password (str): user's password
            first_name (str): user's first name
            last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super(User, self).__init__(**kwargs)
        else:
            super(User, self).__init__()
