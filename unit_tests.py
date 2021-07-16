
import unittest
from lambda_function import River

class Test_river(unittest.TestCase):

    def setUp(self):
        self.river = River()

    def test_river_class(self):
        self.assertIsInstance(self.river, River)

    def test_KM_to_Miles_function(self):
        result = self.river.km_to_miles(6)
        expected = 3.75
        self.assertEqual(result, expected)

    def test_Rating_function(self):
        result = self.river.rating(6,3)
        expected = 5
        self.assertEqual(result, expected)

    def test_River_Grade_function(self):
        result = self.river.river_grade(10)
        expected = "Extreme"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
