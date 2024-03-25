#!/usr/bin/python3

"""writing a test case for the amenity file"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    
    """test cases to check for"""
    
    def test_name(self):
        obj = Amenity()
        self.assertEqual(obj.name, "")