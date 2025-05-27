import unittest
from time_utils import *

class TestTimeUtils(unittest.TestCase):
    def test_seconds_to_minutes(self):
        self.assertEqual(seconds_to_minutes(120), 2.0)
        self.assertEqual(seconds_to_minutes(0), 0.0)

    def test_minutes_to_hours(self):
        self.assertEqual(minutes_to_hours(120), 2.0)
        self.assertEqual(minutes_to_hours(0), 0.0)

    def test_hours_to_days(self):
        self.assertEqual(hours_to_days(48), 2.0)
        self.assertEqual(hours_to_days(0), 0.0)

    def test_add_time_hours(self):
        self.assertEqual(add_time_hours(10, 5), 15)
        self.assertEqual(add_time_hours(0, 0), 0)

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2020))
        self.assertFalse(is_leap_year(2021))

    def test_days_in_month(self):
        self.assertEqual(days_in_month(2, 2020), 29)
        self.assertEqual(days_in_month(4, 2023), 30)

    def test_seconds_to_hms(self):
        self.assertEqual(seconds_to_hms(3661), (1, 1, 1))
        self.assertEqual(seconds_to_hms(0), (0, 0, 0))

    def test_time_difference_hours(self):
        self.assertEqual(time_difference_hours(10, 15), 5)
        self.assertEqual(time_difference_hours(15, 10), 5)

    def test_is_valid_hour(self):
        self.assertTrue(is_valid_hour(23))
        self.assertFalse(is_valid_hour(24))

    def test_format_time_24h(self):
        self.assertEqual(format_time_24h(9, 5), "09:05")
        self.assertEqual(format_time_24h(23, 59), "23:59")

if __name__ == '__main__':
    unittest.main()