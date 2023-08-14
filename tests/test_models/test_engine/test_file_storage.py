import unittest
import os
import json
from models.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class TestFileStorageClass(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialization(self):
        self.assertEqual(self.file_storage._FileStorage__file_path, self.file_path)
        self.assertEqual(self.file_storage._FileStorage__objects, {})

    def test_all(self):
        all_objects = self.file_storage.all()
        self.assertEqual(all_objects, {})

    def test_new(self):
        user = User()
        self.file_storage.new(user)
        all_objects = self.file_storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertIn("User.{}".format(user.id), all_objects)

    def test_save_and_reload(self):
        user = User()
        amenity = Amenity()
        state = State()
        city = City()
        place = Place()
        review = Review()

        self.file_storage.new(user)
        self.file_storage.new(amenity)
        self.file_storage.new(state)
        self.file_storage.new(city)
        self.file_storage.new(place)
        self.file_storage.new(review)
        self.file_storage.save()

        loaded_storage = FileStorage()
        loaded_storage._FileStorage__file_path = self.file_path
        loaded_storage.reload()

        loaded_objects = loaded_storage.all()
        self.assertEqual(len(loaded_objects), 6)
        self.assertIn("User.{}".format(user.id), loaded_objects)
        self.assertIn("Amenity.{}".format(amenity.id), loaded_objects)
        self.assertIn("State.{}".format(state.id), loaded_objects)
        self.assertIn("City.{}".format(city.id), loaded_objects)
        self.assertIn("Place.{}".format(place.id), loaded_objects)
        self.assertIn("Review.{}".format(review.id), loaded_objects)


if __name__ == '__main__':
    unittest.main()
