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
        self.model1.name = 'First model'
        self.model1.number = 8

    def test_instantiation(self):
        """test __init__ method
        """
        self.assertIsInstance(self.model1, BaseModel)
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertFalse(hasattr(self.model1, 'updated_at'))

    
    def test_save(self):
        self.model1.save()
        self.assertTrue(hasattr(self.model1, "updated_at"))
        old_time = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(old_time, self.model1.updated_at)

    def test_to_dict(self):
        self.model1.save()
        created_at_datetime = self.model1.created_at
        self.test_args = self.model1.to_dict()
        self.assertTrue(
            ('id' and 'created_at' and 'updated_at' and 'name' and '__class__' and 'number') in self.test_args.keys())
        self.assertIsInstance(self.test_args['id'], str)
        self.assertIsInstance(self.test_args['__class__'], str)
        self.assertIsInstance(self.test_args['created_at'], str)
        self.assertIsInstance(self.test_args['updated_at'], str)
        self.assertIsInstance(self.test_args['name'], str)
        self.assertIsInstance(self.test_args['number'], int)
        self.assertEqual(datetime.isoformat(created_at_datetime), self.test_args['created_at'])

    def test_reinstantiation(self):
        test_args = self.model1.to_dict()
        self.model2 = BaseModel(**test_args)
        self.model2.save()

        self.assertIsInstance(self.model2, BaseModel)
        self.assertIsInstance(self.model2.created_at, datetime)
        self.assertIsInstance(self.model2.updated_at, datetime)
        self.assertFalse('__class__' in self.model2.__dict__)
        self.assertEqual(test_args['id'], self.model2.id)
        self.assertEqual(datetime.fromisoformat(test_args['created_at']), self.model2.created_at)
        self.assertEqual(test_args['name'], self.model2.name)
        self.assertTrue(test_args['number'], self.model2.number)


if __name__ == '__main__':
    unittest.main()
