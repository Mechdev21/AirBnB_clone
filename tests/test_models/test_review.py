#!/usr/bin/python3

""" Test cases fro the review file"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """writing the test cases"""
    
    def test_place_id(self):
        obj = Review()
        self.assertEqual(obj.place_id, "")
        
    def test_user_id(self):
        obj = Review()
        self.assertEqual(obj.user_id, "")
        
    def test_text(self):
        obj = Review()
        self.assertEqual(obj.text, "")