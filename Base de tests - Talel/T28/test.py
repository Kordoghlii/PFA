import unittest
import math
from geometry_calcs import *

class TestGeometryCalcs(unittest.TestCase):
    def test_sphere_volume(self):
        self.assertAlmostEqual(sphere_volume(2), (4/3) * math.pi * 8)
        self.assertAlmostEqual(sphere_volume(0), 0)

    def test_sphere_surface_area(self):
        self.assertAlmostEqual(sphere_surface_area(2), 4 * math.pi * 4)
        self.assertAlmostEqual(sphere_surface_area(0), 0)

    def test_cylinder_volume(self):
        self.assertAlmostEqual(cylinder_volume(2, 3), math.pi * 4 * 3)
        self.assertAlmostEqual(cylinder_volume(0, 5), 0)

    def test_cone_volume(self):
        self.assertAlmostEqual(cone_volume(2, 3), (1/3) * math.pi * 4 * 3)
        self.assertAlmostEqual(cone_volume(0, 5), 0)

    def test_rectangular_prism_volume(self):
        self.assertEqual(rectangular_prism_volume(2, 3, 4), 24)
        self.assertEqual(rectangular_prism_volume(0, 5, 2), 0)

    def test_triangular_prism_volume(self):
        self.assertEqual(triangular_prism_volume(6, 4), 24)
        self.assertEqual(triangular_prism_volume(0, 5), 0)

    def test_pyramid_volume(self):
        self.assertEqual(pyramid_volume(9, 4), 12)
        self.assertEqual(pyramid_volume(0, 5), 0)

    def test_cube_volume(self):
        self.assertEqual(cube_volume(2), 8)
        self.assertEqual(cube_volume(0), 0)

    def test_ellipsoid_volume(self):
        self.assertAlmostEqual(ellipsoid_volume(2, 3, 4), (4/3) * math.pi * 24)
        self.assertAlmostEqual(ellipsoid_volume(0, 2, 3), 0)

    def test_torus_volume(self):
        self.assertAlmostEqual(torus_volume(1, 3), 2 * math.pi ** 2 * 1 * 4)
        self.assertAlmostEqual(torus_volume(2, 2), 0)

if __name__ == '__main__':
    unittest.main()