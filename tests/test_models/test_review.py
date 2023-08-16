import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    def test_initialization(self):
        review_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'place_id': 'place123',
            'user_id': 'user456',
            'text': 'This place was amazing!'
        }

        review = Review(**review_data)

        self.assertEqual(review.id, 'test_id')
        self.assertEqual(review.created_at, '2023-08-13T12:00:00')
        self.assertEqual(review.place_id, 'place123')
        self.assertEqual(review.user_id, 'user456')
        self.assertEqual(review.text, 'This place was amazing!')

    def test_empty_initialization(self):
        review = Review()

        self.assertEqual(review.id, None)
        self.assertEqual(review.created_at, None)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        review_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'place_id': 'place123',
            'user_id': 'user456',
            'text': 'This place was amazing!'
        }

        review = Review(**review_data)
        review_dict = review.to_dict()

        self.assertEqual(review_dict, review_data)

    def test_str_representation(self):
        review_data = {
            'id': 'test_id',
            'created_at': '2023-08-13T12:00:00',
            'place_id': 'place123',
            'user_id': 'user456',
            'text': 'This place was amazing!'
        }

        review = Review(**review_data)
        review_str = str(review)

        self.assertEqual(review_str, "[Review] (test_id) {'place_id': 'place123', 'user_id': 'user456', 'text': 'This place was amazing!'}")


if __name__ == '__main__':
    unittest.main()
