#!/usr/bin/python3

"""
Testing for the city class
"""
import unittest
from models.city import City



class Test_city(unittest.TestCase):

    def test_empty_string(self):
        obj = City()
        self.assertEqual(obj.state_id, "")

    def test_empty_string_name(self):

        obj = City()
        self.assertEqual(obj.name, "")
