import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_contains_expected_keys(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        obj_dict = self.base_model.to_dict()
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_str_representation(self):
        dictio = self.base_model.__dict__
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, dictio)
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
