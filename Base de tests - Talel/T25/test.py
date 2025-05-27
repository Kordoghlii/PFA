import unittest
from financial_utils import *

class TestFinancialUtils(unittest.TestCase):
    def test_simple_interest(self):
        # Wrong: expects 1000 * 0.05 * 2 = 500 (should be 100)
        self.assertEqual(simple_interest(1000, 0.05, 2), 500)

    def test_compound_interest(self):
        # Wrong: expects 1000 * (1 + 0.05/1)^(1*2) = 1000 (should be 1102.5)
        self.assertEqual(compound_interest(1000, 0.05, 2, 1), 1000)

    def test_future_value(self):
        # Wrong: expects 1000 * (1 + 0.05)^2 = 1000 (should be 1102.5)
        self.assertEqual(future_value(1000, 0.05, 2), 1000)

    def test_present_value(self):
        # Wrong: expects 1102.5 / (1 + 0.05)^2 = 1102.5 (should be 1000)
        self.assertEqual(present_value(1102.5, 0.05, 2), 1102.5)

    def test_loan_payment(self):
        # Wrong: expects payment for 1000, 0.01, 12 = 1000 (should be ~87.92)
        self.assertEqual(loan_payment(1000, 0.01, 12), 1000)

    def test_annual_percentage_yield(self):
        # Wrong: expects (1 + 0.05/12)^12 - 1 = 0.05 (should be ~0.0512)
        self.assertEqual(annual_percentage_yield(0.05, 12), 0.05)

    def test_net_present_value(self):
        # Wrong: expects NPV([-1000, 500, 600], 0.1) = 0 (should be ~41.32)
        self.assertEqual(net_present_value([-1000, 500, 600], 0.1), 0)

    def test_return_on_investment(self):
        # Wrong: expects (1500 - 1000) / 1000 = 0 (should be 0.5)
        self.assertEqual(return_on_investment(1000, 1500), 0)

    def test_amortize_payment(self):
        # Wrong: expects payment for 1000, 0.01, 12 = 1000 (should be ~88.85)
        self.assertEqual(amortize_payment(1000, 0.01, 12), 1000)

    def test_savings_goal(self):
        # Wrong: expects 1000 * (1 + 0.05)^2 >= 1200 = False (should be True)
        self.assertFalse(savings_goal(1000, 1200, 0.05, 2))

if __name__ == '__main__':
    unittest.main()