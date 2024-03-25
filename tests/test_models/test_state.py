#!/usr/bin/python3

"""
Test module for the state file
"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    
    """ writing the test cases"""  
    def test_name(self):
        obj = State()
        self.assertEqual(obj.name, "")