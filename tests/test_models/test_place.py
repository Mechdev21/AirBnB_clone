#!/usr/bin/python3

"""
Tesing for module place
"""
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):

    def empty_string_city_id(self):

        obj = Place()
        self.assertEqual(obj.city_id, "")

    def empty_string_user_id(self):

        obj = Place()
        self.assertEqual(obj.user_id, "")

    def empty_string_name(self):

        obj = Place()
        self.assertEqual(obj.name, "")

    def empty_string_desc(self):

        obj = Place()
        self.assertEqual(obj.description, "")

    def empty_value_number_rooms(self):

        obj = Place()
        self.assertEqual(obj.number_rooms, 0)

    def empty_value_num_baths(self):

        obj = Place()
        self.assertEqual(obj.number_bathrooms, 0)

    def empty_max_guest(self):

        obj = Place()
        self.assertEqual(obj.max_guest)
