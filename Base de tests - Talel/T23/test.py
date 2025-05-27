import unittest
from date_utils import *

class TestDateUtils(unittest.TestCase):
    def test_is_valid_date(self):
        self.assertTrue(is_valid_date(15, 6, 2023))
        self.assertFalse(is_valid_date(30, 2, 2023))

    def test_day_of_week(self):
        self.assertEqual(day_of_week(15, 6, 2023), 3)  # Thursday
        self.assertEqual(day_of_week(1, 1, 2023), 6)  # Sunday

    def test_days_between_dates(self):
        self.assertEqual(days_between_dates(1, 1, 2023, 2, 1, 2023), 1)
        self.assertEqual(days_between_dates(1, 1, 2023, 1, 1, 2024), 365)

    def test_add_days(self):
        self.assertEqual(add_days(31, 12, 2022, 1), (1, 1, 2023))
        self.assertEqual(add_days(1, 1, 2023, 0), (1, 1, 2023))

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2020))
        self.assertFalse(is_leap_year(2021))

    def test_days_in_year(self):
        self.assertEqual(days_in_year(2020), 366)
        self.assertEqual(days_in_year(2021), 365)

    def test_next_day(self):
        self.assertEqual(next_day(31, 12, 2022), (1, 1, 2023))
        self.assertEqual(next_day(28, 2, 2023), (1, 3, 2023))

    def test_is_weekend(self):
        self.assertTrue(is_weekend(17, 6, 2023))  # Saturday
        self.assertFalse(is_weekend(15, 6, 2023))  # Thursday

    def test_month_name(self):
        self.assertEqual(month_name(1), "January")
        self.assertEqual(month_name(13), "")

    def test_days_in_month(self):
        self.assertEqual(days_in_month(2, 2020), 29)
        self.assertEqual(days_in_month(4, 2023), 30)

if __name__ == '__main__':
    unittest.main()