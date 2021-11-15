#!/usr/bin/python3
"""
User Module AirBnB Backend
"""
from models import *


class Amenity(BaseModel):
    """Amenity Model

    Args:
        BaseModel (class object BaseModel): BaseModel object class
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
