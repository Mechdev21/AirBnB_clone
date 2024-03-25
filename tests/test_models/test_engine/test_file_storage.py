#!/usr/bin/python3
"""Testing Engine"""

import json
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """testing filestorage"""

    def test_A_type(self):
        self.assertEqual(FileStorage, type(FileStorage()))
    def test_B_classatrr(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
