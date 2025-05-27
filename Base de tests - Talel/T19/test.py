import unittest
from conversion_utils import *

class TestConversionUtils(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # Wrong: expects 0°C = 0°F (should be 32°F)
        self.assertEqual(celsius_to_fahrenheit(0), 0)

    def test_fahrenheit_to_celsius(self):
        # Wrong: expects 32°F = 32°C (should be 0°C)
        self.assertEqual(fahrenheit_to_celsius(32), 32)

    def test_meters_to_feet(self):
        # Wrong: expects 1m = 1ft (should be ~3.28084ft)
        self.assertEqual(meters_to_feet(1), 1)

    def test_feet_to_meters(self):
        # Wrong: expects 3.28084ft = 3.28084m (should be 1m)
        self.assertEqual(feet_to_meters(3.28084), 3.28084)

    def test_kg_to_pounds(self):
        # Wrong: expects 1kg = 1lb (should be ~2.20462lb)
        self.assertEqual(kg_to_pounds(1), 1)

    def test_pounds_to_kg(self):
        # Wrong: expects 2.20462lb = 2.20462kg (should be 1kg)
        self.assertEqual(pounds_to_kg(2.20462), 2.20462)

    def test_km_to_miles(self):
        # Wrong: expects 1km = 1mi (should be ~0.621371mi)
        self.assertEqual(km_to_miles(1), 1)

    def test_miles_to_km(self):
        # Wrong: expects 1mi = 1km (should be ~1.60934km)
        self.assertEqual(miles_to_km(1), 1)

    def test_liters_to_gallons(self):
        # Wrong: expects 1L = 1gal (should be ~0.264172gal)
        self.assertEqual(liters_to_gallons(1), 1)

    def test_gallons_to_liters(self):
        # Wrong: expects 1gal = 1L (should be ~3.78541L)
        self.assertEqual(gallons_to_liters(1), 1)

if __name__ == '__main__':
    unittest.main()