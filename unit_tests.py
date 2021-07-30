'''
PJones - bh83dq
20/07/2021
Unit tests for the lambda function
'''

import unittest
from lambda_function import River


class TestRiver(unittest.TestCase):
    '''
    test Class to hold unit tests for Lambda Function
    '''
    def setUp(self):
        self.river = River()

    def test_river_class(self):
        '''
        test function to check class exists
        '''
        self.assertIsInstance(self.river, River)

    def test_km_to_miles_function(self):
        '''
        test function to check measurement conversion
        '''
        result = self.river.km_to_miles(6)
        expected = 3.75
        self.assertEqual(result, expected)

    def test_rating_function(self):
        '''
        test function to check rating function
        '''
        result = self.river.rating(6, 3)
        expected = 5
        self.assertEqual(result, expected)

    def test_river_grade_function(self):
        '''
        test function to check grade function
        '''
        result = self.river.river_grade(10)
        expected = "Too Extreme"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
