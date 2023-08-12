import unittest
from unittest.mock import patch
import json
import os
from models.engine.file_storage import FileStorage


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
        test_obj = {'__class__': 'TestClass', 'id': 'test_id'}
        self.file_storage.new(test_obj)
        self.assertIn('TestClass.test_id', self.file_storage.all())

    def test_save_writes_to_file(self):
        test_obj = {'__class__': 'TestClass', 'id': 'test_id'}
        self.file_storage.new(test_obj)
        self.file_storage.save()

        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.assertIn('TestClass.test_id', data)

    def test_reload_loads_from_file(self):
        test_obj = {'__class__': 'TestClass', 'id': 'test_id'}
        self.file_storage.new(test_obj)
        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage.reload()

        self.assertIn('TestClass.test_id', new_file_storage.all())

    @patch('os.path.exists')
    def test_reload_does_not_fail_if_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        self.file_storage.reload()

    @patch('os.path.exists')
    def test_reload_does_not_fail_on_empty_file(self, mock_exists):
        mock_exists.return_value = True
        with open(self.file_path, 'w') as f:
            f.write('')
        self.file_storage.reload()


if __name__ == '__main__':
    unittest.main()

