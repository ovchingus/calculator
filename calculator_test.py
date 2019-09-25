import calculator
import unittest

class TestCalculator(unittest.TestCase):
  def test_plus(self):
    self.assertEqual(calculator.plus(12,4), 12 + 4)

  def test_plus(self):
    self.assertEqual(calculator.minus(12,4), 12 - 4)

  def test_plus(self):
    self.assertEqual(calculator.multiply(12,4), 12 * 4)

  def test_plus(self):
    self.assertEqual(calculator.divide(12,4), 12 / 4)

if __name__ == '__main__':
  unittest.main()