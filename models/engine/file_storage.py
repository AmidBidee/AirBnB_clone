#!/usr/bin/python3
"""
file storage module for AirBnB project
"""

import json
from datetime import datetime

class FileStorage:
    """
    File storage class

    Attributes:
        [private]:
            __file_path[str]: filename
            __objects[dict]: dictionary representing 
                             stored objects
        [public]:
            all(self)
            new(self, obj)
            save(self)
            reload(self)
            
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self, *args, **kwargs):
        """
        instantiate file storage class
        """
        pass

    def all(self):
        """
        returns the dictionary __objects

        Returns:
            __objects[dict]: dictionary representing all saved
                             instances
        """
        return self.__objects

    def new(self, obj):
        """

        Args:
            obj[class]: object to be stored
        """
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        """
        writes serialized objects in self.__objects into json file
        """
        temp = {}

        for k in self.__objects.keys():
            temp[k] = self.__objects[k].to_dict()

        with open(FileStorage.__file_path, 'w', encodeing='utf8') as fd:
            fd.write(json.dumps(temp))

    def reload(self):
        """
        reloads and recreates objects from a json file
        """

        try:
            FileStorage.__objects = {}
            
            with open(FileStorage.__file_path, 'r', encoding='utf8') as fd:
                file_objects = json.loads(fd)

            for k in file_objects.keys():
                if k not in ('__class__', 'created_at', 'updated_at'):
                    FileStorage.__objects[k] = file_objects[k]
                else:
                    if k in ('created_at', 'updated_at'):
                        FileStorage.__objects[k] = datetime.fromisoformat(file_objects[k])
        except Exception as e:
            print(e)
            pass
