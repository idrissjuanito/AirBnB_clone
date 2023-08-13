import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    def test_initialization(self):
        amenity_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'Wifi'
        }

        amenity = Amenity(**amenity_data)

        self.assertEqual(amenity.id, 'test_id')
        self.assertEqual(amenity.created_at, '2023-08-13T12:00:00')
        self.assertEqual(amenity.name, 'Wifi')

    def test_empty_initialization(self):
        amenity = Amenity()

        self.assertEqual(amenity.id, None)
        self.assertEqual(amenity.created_at, None)
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        amenity_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'Wifi'
        }

        amenity = Amenity(**amenity_data)
        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict, amenity_data)

    def test_str_representation(self):
        amenity_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'Wifi'
        }

        amenity = Amenity(**amenity_data)
        amenity_str = str(amenity)

        self.assertEqual(amenity_str, "[Amenity] (test_id) {'name': 'Wifi'}")


if __name__ == '__main__':
    unittest.main()
