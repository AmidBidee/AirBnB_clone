#!/usr/bin/python3
"""
place Module AirBnB Backend
"""
from models import *


class Place(BaseModel):
    """
    Place Model
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenities = [""]

    def __init__(self, *args, **kwargs):
        """
        Initializes Place Model and calls super class init method
        """
        super().__init__(*args, **kwargs)
