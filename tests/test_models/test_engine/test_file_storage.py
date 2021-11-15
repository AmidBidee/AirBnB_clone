#!/usr/bin/python3
"""FileStorage TestCase module for AirBnB clone
"""

import unittest
import os
from datetime import datetime
import json
from models.engine.file_storage import FileStorage
from models import *


class Test_FileStorage(unittest.TestCase):
    """
    Test the file storage class
    """

    def setUp(self):
        """Setup Tests data
        """
        self.store = FileStorage()

        test_args = {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381",
                     "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}
        self.model = BaseModel(**test_args)

    def tearDown(self):
        """
        deletes file created
        """
        if os.path.isfile("file.json"):
            os.remove('file.json')

    def test_all(self):
        """
        Tests all method
        """
        self.assertEqual(len(self.store.all()), 0)

    def test_new(self):
        """
        Tests new method
        """
        self.assertEqual(len(self.store.all()), 0)
        a = BaseModel()
        self.assertEqual(len(self.store.all()), 1)
        a.save()

    def test_save(self):
        """
        tests save method
        """
        a_new = BaseModel()
        self.store.save()
        with open('file.json', 'r', encoding='utf8') as fd:
            d = json.load(fd)

        self.assertTrue(f'BaseModel.{a_new.id}' in d.keys())
        #b = User()
        #self.assertNotEqual(len(self.store.all()), self.test_len + 2)
        # b.save()
        #self.assertEqual(len(self.store.all()), self.test_len + 2)

    def test_reload(self):
        """Tests reload method
        """
        pass


if __name__ == "__main__":
    unittest.main()
