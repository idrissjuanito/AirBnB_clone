import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    def test_initialization(self):
        place_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'Cozy Cottage',
            'user_id': 'user123',
            'city_id': 'city456',
            'description': 'A comfortable place to relax',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 42.12345,
            'longitude': -71.98765,
            'amenity_ids': ['amenity1', 'amenity2']
        }

        place = Place(**place_data)

        self.assertEqual(place.id, 'test_id')
        self.assertEqual(place.created_at, '2023-08-13T12:00:00')
        self.assertEqual(place.name, 'Cozy Cottage')
        self.assertEqual(place.user_id, 'user123')
        self.assertEqual(place.city_id, 'city456')
        self.assertEqual(place.description, 'A comfortable place to relax')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 42.12345)
        self.assertEqual(place.longitude, -71.98765)
        self.assertEqual(place.amenity_ids, ['amenity1', 'amenity2'])

    def test_empty_initialization(self):
        place = Place()

        self.assertEqual(place.id, None)
        self.assertEqual(place.created_at, None)
        self.assertEqual(place.name, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict(self):
        place_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'Cozy Cottage',
            'user_id': 'user123',
            'city_id': 'city456',
            'description': 'A comfortable place to relax',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 42.12345,
            'longitude': -71.98765,
            'amenity_ids': ['amenity1', 'amenity2']
        }

        place = Place(**place_data)
        place_dict = place.to_dict()

        self.assertEqual(place_dict, place_data)

    def test_str_representation(self):
        place_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'Cozy Cottage',
            'user_id': 'user123',
            'city_id': 'city456',
            'description': 'A comfortable place to relax',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 42.12345,
            'longitude': -71.98765,
            'amenity_ids': ['amenity1', 'amenity2']
        }

        place = Place(**place_data)
        place_str = str(place)

        self.assertEqual(place_str, "[Place] (test_id) {'name': 'Cozy Cottage', 'user_id': 'user123', 'city_id': 'city456', 'description': 'A comfortable place to relax', 'number_rooms': 2, 'number_bathrooms': 1, 'max_guest': 4, 'price_by_night': 100, 'latitude': 42.12345, 'longitude': -71.98765, 'amenity_ids': ['amenity1', 'amenity2']}")

if __name__ == '__main__':
    unittest.main()
