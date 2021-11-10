"""Amenity TestCase module
"""
import unittest
from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    """Test the amenity model

    Args:
        unittest (unittest.TestCase): TestCase inherited from unittest module
    """

    def setUp(self):
        self.model = Amenity()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, 'name'))
        self.assertEqual(self.model.name, '')


if __name__ == '__main__':
    unittest.main()
