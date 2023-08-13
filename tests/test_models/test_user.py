#!/usr/bin/python3
""" Test Module for User class """
import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """ test cases for User class attributes and methods """
    def test_initialization(self):
        user_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'email': 'test@example.com',
            'password': 'testpass',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        user = User(**user_data)

        self.assertEqual(user.id, 'test_id')
        self.assertEqual(user.created_at, '2023-08-13T12:00:00')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'testpass')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_empty_initialization(self):
        user = User()

        self.assertEqual(user.id, None)
        self.assertEqual(user.created_at, None)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        user_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'email': 'test@example.com',
            'password': 'testpass',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        user = User(**user_data)
        user_dict = user.to_dict()

        self.assertEqual(user_dict, user_data)

    def test_str_representation(self):
        user_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'email': 'test@example.com',
            'password': 'testpass',
            'first_name': 'John',
            'last_name': 'Doe'
        }

        user = User(**user_data)
        user_str = str(user)

        fn = "'first_name': 'John'"
        ln = "'last_name': 'Doe'"
        mail = "'email': 'test@example.com'"
        pw = "'password': 'testpass'"
        result = "[User] (test_id) {"+mail+", "+pw+", "+fn+", "+ln+"}"
        self.assertEqual(user_str, result)


if __name__ == '__main__':
    unittest.main()
