import unittest
from unittest.mock import patch, mock_open
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        self.file_storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_objects_dict(self):
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(objects, FileStorage._FileStorage__objects)

    def test_new_adds_object_to_objects_dict(self):
        test_obj = BaseModel()
        self.file_storage.new(test_obj)
        self.assertIn(f'{test_obj.__class__.__name__}.{test_obj.id}', self.file_storage.all())

    @patch('json.dump')
    def test_save_writes_to_file(self, mock_json_dump):
        test_obj = BaseModel()
        self.file_storage.new(test_obj)
        self.file_storage.save()

        mock_json_dump.assert_called_once()

    @patch('json.load', return_value={'BaseModel.test_id': {'id': 'test_id'}})
    def test_reload_loads_from_file(self, mock_json_load):
        self.file_storage.reload()

        self.assertIn('BaseModel.test_id', self.file_storage.all())

    @patch('os.path.exists')
    def test_reload_does_not_fail_if_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        self.file_storage.reload()

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_reload_does_not_fail_on_empty_file(self, mock_open_file, mock_exists):
        mock_exists.return_value = True
        self.file_storage.reload()

        mock_open_file.assert_called_once()


if __name__ == '__main__':
    unittest.main()
