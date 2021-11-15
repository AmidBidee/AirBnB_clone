#!/usr/bin/python3
"""
state module
"""
from models import *


class State(BaseModel):
    """State Model

    Args:
        BaseModel ([type]): [description]
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes State Model and calls super class init method
        """
        super(State, self).__init__(*args, **kwargs)
