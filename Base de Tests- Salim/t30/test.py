import unittest
import math
from geometry_utils import *

class TestGeometryUtils(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(2), math.pi * 4)
        self.assertAlmostEqual(circle_area(0), 0)

    def test_circle_circumference(self):
        self.assertAlmostEqual(circle_circumference(2), 2 * math.pi * 2)
        self.assertAlmostEqual(circle_circumference(0), 0)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(3, 4), 14)
        self.assertEqual(rectangle_perimeter(0, 0), 0)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(4, 3), 6)
        self.assertEqual(triangle_area(0, 5), 0)

    def test_is_right_triangle(self):
        self.assertTrue(is_right_triangle(3, 4, 5))
        self.assertFalse(is_right_triangle(1, 1, 1))

    def test_distance_2d(self):
        self.assertAlmostEqual(distance_2d(0, 0, 3, 4), 5)
        self.assertAlmostEqual(distance_2d(1, 1, 1, 1), 0)

    def test_slope(self):
        self.assertEqual(slope(0, 0, 2, 4), 2)
        self.assertIsNone(slope(1, 2, 1, 5))

    def test_is_collinear(self):
        self.assertTrue(is_collinear(0, 0, 1, 1, 2, 2))
        self.assertFalse(is_collinear(0, 0, 1, 1, 2, 0))

if __name__ == '__main__':
    unittest.main()