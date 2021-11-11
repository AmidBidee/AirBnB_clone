"""Module for BaseModel
"""

import uuid
import datetime
import json

now = datetime.datetime.now

class BaseModel:
    """Base Model for Future Models
    """

    def __init__(self, *args, **kwargs):
        if args:
            
        pass

    def save(self):
        pass

    def to_dict(self):
        pass