"""Module for BaseModel
"""

import datetime
import json
import uuid

now = datetime.datetime.now()

class BaseModel:
    """
    Base Model for Future Models
    """

    def __init__(self, *args, **kwargs):
        """
        initialize base model
        """
        self.id = str(uuid.uuid4())
        self.created_at = now

        if kwargs:
            for k in kwargs.keys():
                if k not in ('__class__', 'created_at', 'updated_at'):
                    setattr(self, k, kwargs[k])
                else:
                    if k in ('created_at', 'updated_at'):
                        setattr(self, k, datetime.datetime.fromisoformat(kwargs[k]))
            

    def save(self):
        """
        updates the public instance attribute updated_at
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns dictionary representation of the instance

        Returns:
            dict: representation of the instance
        """
        _dict = {'__class__': self.__class__.__name__}

        m_dict = self.__dict__
        for k in m_dict.keys():
            if k not in ('created_at', 'updated_at'):
                _dict[k] = m_dict[k]
            else:
                _dict[k] = datetime.datetime.isoformat(m_dict[k])

        return _dict

    def __str__(self):
        """String representation of object

        Returns:
            str: representation of object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    @staticmethod
    def to_json():
        pass
