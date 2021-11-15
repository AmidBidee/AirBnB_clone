#!/usr/bin/python3
"""
user module
"""

from models import *


class User(BaseModel):
    """User Model

    Args:
        BaseModel ([type]): [description]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes User Model and calls super class init method
        """
        super().__init__(*args, **kwargs)
