#!/usr/bin/python3

"""
Tesing for module place
"""
import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """
    I could have just used the superUp() to write
    the object instantiation
    
    'def superUp(self):
    obj = Place().
    
    instead of repeating it in the code
    """

    def empty_string_city_id(self):

        obj = Place()
        self.assertEqual(obj.city_id, "")

    def test_empty_string_user_id(self):

        obj = Place()
        self.assertEqual(obj.user_id, "")

    def test_empty_string_name(self):

        obj = Place()
        self.assertEqual(obj.name, "")

    def test_empty_string_desc(self):

        obj = Place()
        self.assertEqual(obj.description, "")

    def test_empty_value_number_rooms(self):

        obj = Place()
        self.assertEqual(obj.number_rooms, 0)

    def test_empty_value_num_baths(self):

        obj = Place()
        self.assertEqual(obj.number_bathrooms, 0)

    def test_empty_max_guest(self):

        obj = Place()
        self.assertEqual(obj.max_guest, 0)
        
    def test_empty_price_by_night(self):
        
        obj = Place()
        self.assertEqual(abj.price_by_night, 0)
        
    def test_latitude(self):
        
        obj = Place()
        self.assertEqual(obj.latitude, 0.0)
        
    def test_longitude(self):
        
        obj = Place()
        self.assertEqual(obj.longitude, 0.0)
        
    def test_amenity_ids(self):
        
        obj = Place()
        self.assertGreaterEqual(obj.amenity_ids, "")