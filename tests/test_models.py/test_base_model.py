#!/usr/bin/python3
"""
writing a test for the Basemodel

Unitest classes:
        TestBaseModels_instantiation
        TestBaseModel_save
        TEstBaseModel_to_dict
"""

import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModels_instantiation(unittest.TestCase):
    """Testing the instantiatioin of the BaseModel class"""

    def test_new_instance_stored_in_objects(self):
        self.assertEqual(Basemodel, models.storage.all().values())

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_for_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_id_is_unique(self):
        bmodel1 = BaseModel()
        bmodel2 = BaseModel()
        self.assertnotEqual(bamodel1.id, bmodel2.id)

    def test_two_models_different_created_at(self):
        bmodel1 = BaseModel()
        sleep(0.06)
        bmodel2 = BaseModel()
        self.assertLess(bmodel1.created_at, bmodel2.createdat)

    def test_two_models_different_updated_at(self):
        bmodel1 = BaseModel()
        sleep(0.06)
        bmodel2 = BaseModel()
        self.assertLess(bmodel1.updated_at, bmodel2.updated_at)

    def test_args_unsued(self):
        bmodel = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_str_representation(self):
        dd = datetime.today()
        dd_rep = repr(dd)
        bmodel = BaseModel()
        bmodel.id = "123456"
        bmodel.created_at = bmodel.updated_at = dd
        bmodelstr = bmodel.__str__()
        self.assertIn("[BaseModel] (123456)", bmodelstr)
        self.assertIn("'id': '123456'", bmodelstr)
        self.assertIn("'created_at': " + dd_rep, bmodelstr)
        self.assertIn("'updated_at': " + dd_rep, bmodelstr)

    def test_instantiation_with_args_and_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=none, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
