import unittest
from color_utils import *

class TestColorUtils(unittest.TestCase):
    def test_rgb_to_hex(self):
        # Wrong: expects (255, 0, 0) = "#000000" (should be "#FF0000")
        self.assertEqual(rgb_to_hex(255, 0, 0), "#000000")

    def test_hex_to_rgb(self):
        # Wrong: expects "#FF0000" = (0, 0, 0) (should be (255, 0, 0))
        self.assertEqual(hex_to_rgb("#FF0000"), (0, 0, 0))

    def test_clamp_color(self):
        # Wrong: expects 300 = 0 (should be 255)
        self.assertEqual(clamp_color(300), 0)

    def test_brighten_rgb(self):
        # Wrong: expects (100, 100, 100) * 1.5 = (100, 100, 100) (should be (150, 150, 150))
        self.assertEqual(brighten_rgb(100, 100, 100, 1.5), (100, 100, 100))

    def test_darken_rgb(self):
        # Wrong: expects (100, 100, 100) * 0.5 = (100, 100, 100) (should be (50, 50, 50))
        self.assertEqual(darken_rgb(100, 100, 100, 0.5), (100, 100, 100))

    def test_rgb_to_grayscale(self):
        # Wrong: expects (255, 0, 0) = (0, 0, 0) (should be ~76, 76, 76)
        self.assertEqual(rgb_to_grayscale(255, 0, 0), (0, 0, 0))

    def test_is_valid_rgb(self):
        # Wrong: expects (0, 255, 255) = False (should be True)
        self.assertFalse(is_valid_rgb(0, 255, 255))

    def test_blend_colors(self):
        # Wrong: expects blend (255, 0, 0) and (0, 255, 0) at 0.5 = (0, 0, 0) (should be ~127, 127, 0)
        self.assertEqual(blend_colors((255, 0, 0), (0, 255, 0), 0.5), (0, 0, 0))

    def test_rgb_to_hsv(self):
        # Wrong: expects (255, 0, 0) = (0, 0, 0) (should be (0, 1, 1))
        self.assertEqual(rgb_to_hsv(255, 0, 0), (0, 0, 0))

    def test_complementary_color(self):
        # Wrong: expects (255, 0, 0) = (0, 0, 0) (should be (0, 255, 255))
        self.assertEqual(complementary_color(255, 0, 0), (0, 0, 0))

if __name__ == '__main__':
    unittest.main()