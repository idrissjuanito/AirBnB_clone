import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    def test_initialization(self):
        state_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'California'
        }

        state = State(**state_data)

        self.assertEqual(state.id, 'test_id')
        self.assertEqual(state.created_at, '2023-08-13T12:00:00')
        self.assertEqual(state.name, 'California')

    def test_empty_initialization(self):
        state = State()

        self.assertEqual(state.id, None)
        self.assertEqual(state.created_at, None)
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        state_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'California'
        }

        state = State(**state_data)
        state_dict = state.to_dict()

        self.assertEqual(state_dict, state_data)

    def test_str_representation(self):
        state_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'name': 'California'
        }

        state = State(**state_data)
        state_str = str(state)

        self.assertEqual(state_str, "[State] (test_id) {'name': 'California'}")


if __name__ == '__main__':
    unittest.main()
