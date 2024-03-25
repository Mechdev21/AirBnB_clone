#!/usr/bin/python3
"""test model for file_storage"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_File_Storage(unittest.TestCase):
    """Testing file storage"""

    def test_A_type_file_storage(self):
        storage = FileStorage()
        self.assertEqual(type(FileStorage), type)
    def test_B_check_class_method(self):
        storage = FileStorage()
        self.assertTrue(storage.all())
