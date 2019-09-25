import calculator
import unittest

calc = calculator.Calculator('base')

class TestCalculator(unittest.TestCase):
  def test_plus(self):
    self.assertEqual(calc.plus(12,4), 12 + 4)

  def test_minus(self):
    self.assertEqual(calc.minus(12,4), 12 - 4)

  def test_multiply(self):
    self.assertEqual(calc.multiply(12,4), 12 * 4)

  def test_divide(self):
    self.assertEqual(calc.divide(12,4), 12 / 4)

if __name__ == '__main__': 
  unittest.main()