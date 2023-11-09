import unittest
from src.calculator import calculate_gas_cost, calculate_loan_payment, calculate_total_monthly_cost

class TestCalculator(unittest.TestCase):

    def test_calculate_gas_cost(self):
        # Assuming calculate_gas_cost takes average miles per gallon, 
        # average miles driven per week, and current gas price per gallon as arguments.
        self.assertAlmostEqual(calculate_gas_cost(25, 300, 3), 36)

    def test_calculate_loan_payment(self):
        # Assuming calculate_loan_payment takes the loan amount, 
        # annual interest rate, and loan term in years as arguments.
        self.assertAlmostEqual(calculate_loan_payment(20000, 0.05, 5), 377.42, places=2)

    def test_calculate_total_monthly_cost(self):
        # Assuming calculate_total_monthly_cost takes the loan payment, 
        # gas cost, and expected monthly maintenance cost as arguments.
        self.assertAlmostEqual(calculate_total_monthly_cost(377.42, 36, 50), 463.42)

if __name__ == '__main__':
    unittest.main()
