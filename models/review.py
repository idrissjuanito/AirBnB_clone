#!/usr/bin/python3
""" Review module for managing reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        Review class for creating new reviews
        Attributes:
            place_id (str): id of place Reviewed is
            user_id (str): name of user made review
            text (str): content of the review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super(Review, self).__init__(**kwargs)
        else:
            super(Review, self).__init__()
