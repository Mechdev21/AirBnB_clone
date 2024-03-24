#!/usr/bin/python3

"""Writing test file for the user file"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """test cases to consider"""
    
    def setUp(self):
        obj = User()
        
    def test_email(self):
        self.assertEqual(obj.email, "")
        
    def test_password(self):
        self.assertEqual(obj.password, "")
        
    def test_first_name(self):
        self.assertEqual(obj.first_name, "")
        
    def test_last_name(self):
        seslf.assertEqual(obj.last_name, "")