#!/usr/bin/python3
"""
review Module AirBnB Backend
"""
from models import *


class Review(BaseModel):
    """Review Model

    Args:
        BaseModel ([type]): [description]
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Review Model and calls super class init method
        """
        super().__init__(*args, **kwargs)
