import calculator
import unittest
import math

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

  def test_sin(self):
    self.assertEqual(calc.sin(10), math.sin(10))

  def test_cos(self):
    self.assertEqual(calc.cos(10), math.cos(10))

  def test_tan(self):
    self.assertEqual(calc.tan(10), math.tan(10))

  def test_asin(self):
    self.assertEqual(calc.asin(10), math.asin(10))

  def test_acos(self):
    self.assertEqual(calc.acos(10), math.acos(10))
  
  def test_atan(self):
    self.assertEqual(calc.atan(10), math.atan(10))
if __name__ == '__main__': 
  unittest.main()