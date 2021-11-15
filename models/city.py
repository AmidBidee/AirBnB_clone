#!/usr/bin/python3
"""
city Module AirBnB Backend
"""

from models import *


class City(BaseModel):
    """
    City Model
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes objects as well as calls super class
            init method and passes in arguments
        """
        super().__init__(*args, **kwargs)
