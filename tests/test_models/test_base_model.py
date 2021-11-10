"""BaseModel Test case module
"""

import unittest
from datetime import datetime
from models import *


class Test_BaseModel(unittest.TestCase):
    """Test the base model class

    Args:
        unittest (unittest.TestCase): TestCase inherited from unittest module
    """

    def setUp(self):
        """set up TestCase with some models and args
        """
        self.model1 = BaseModel()
        test_args = {'created_at': datetime(2021, 11, 10, 2, 6, 55, 258849),
                     'updated_at': datetime(2021, 11, 10, 2, 6, 55, 258966),
                     'id': '46458416-e5d5-4985-aa48-a2b369d03d2a',
                     'name': 'model1'}
        self.model2 = BaseModel(test_args)
        self.model2.save()

    def test_instantiation(self):
        """test __init__ method
        """
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, 'updated_at'))

    def test_reinstantiation(self):
        self.assertIsInstance(self.model2, BaseModel)
        self.assertEqual(
            self.model2.id, '46458416-e5d5-4985-aa48-a2b369d03d2a')
        self.assertEqual(self.model2.created_at, datetime(
            2021, 11, 10, 2, 6, 55, 258849))

    def test_save(self):
        self.assertFalse(hasattr(self.model1, "updated_at"))
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model2.updated_at
        self.model2.save()
        self.assertNotEqual(old_time, self.model2.updated_at)

    def test_to_json(self):
        serialized = self.model2.to_json()
        self.assertNotEqual(self.model2.__dict__, serialized)
        self.assertNotIsInstance(serialized['created_at'], datetime)
        self.assertNotIsInstance(serialized['updated_at'], datetime)
        self.assertEqual(serialized['created_at'],
                         '2021-11-10 02:06:55.258849')
        self.assertTrue(hasattr(serialized, '__class__'))
        self.assertEqual(serialized['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
