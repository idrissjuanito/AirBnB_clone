<<<<<<< HEAD
=======
#!/usr/bin/python3
""" test module for city class """
>>>>>>> 48ccca7db0dfc31f9f251a04ab245935b9ac762e
import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
<<<<<<< HEAD
    def test_initialization(self):
        city_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'New York',
            'state_id': 'NY'
        }

        city = City(**city_data)

        self.assertEqual(city.id, 'test_id')
        self.assertEqual(city.created_at, '2023-08-13T12:00:00')
        self.assertEqual(city.name, 'New York')
        self.assertEqual(city.state_id, 'NY')

    def test_empty_initialization(self):
        city = City()

        self.assertEqual(city.id, None)
        self.assertEqual(city.created_at, None)
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_to_dict(self):
        city_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'New York',
            'state_id': 'NY'
        }

        city = City(**city_data)
        city_dict = city.to_dict()

        self.assertEqual(city_dict, city_data)

    def test_str_representation(self):
        city_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'New York',
            'state_id': 'NY'
        }

        city = City(**city_data)
        city_str = str(city)

        self.assertEqual(city_str, "[City] (test_id) {'name': 'New York', 'state_id': 'NY'}")


if __name__ == '__main__':
    unittest.main()
=======
    """ Test cases for attributes and methods in city class """
    def test_city_name(self):
        pass
>>>>>>> 48ccca7db0dfc31f9f251a04ab245935b9ac762e
