#!/usr/bin/python3
"""
file storage module for AirBnB project
"""

from datetime import datetime
import json

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
        if obj is not None and obj is not dict:
            FileStorage.__objects['BaseModel.' + obj.id] = obj

    def save(self):
        """
        writes serialized objects in self.__objects into json file
        """
        temp = {}

        for k in self.__objects.keys():
            if type(self.__objects[k]) != dict:
                temp[k] = self.__objects[k].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf8') as fd:
            fd.write(json.dumps(temp))

    def reload(self):
        """
        reloads and recreates objects from a json file
        """

        try:
            FileStorage.__objects = {}
            with open(FileStorage.__file_path, 
                    mode="r+", encoding="utf-8") as fd:
                dict_objs = json.loads(fd.read())

            for k in dict_objs.keys():
                dict_objs[k].pop('__class__', None)
                FileStorage.__objects[k] = dict_objs[k]
                for k_i in dict_objs[k].keys():
                    if k_i in ('created_at', 'updated_at'):
                        FileStorage.__objects[k][k_i] = datetime.fromisoformat(dict_objs[k][k_i])
        except Exception as e:
            pass
