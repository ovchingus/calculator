import parser
import unittest

prs = parser.Parser()

class TestInputOutput(unittest.TestCase):
  def test_parse(self):
    self.assertEqual(prs.parseBase('12 + 4'), ['12', '+', '4'])

  def test_parse1(self):
    self.assertEqual(prs.parseBase('12 * 4'), ['12', '*', '4'])

  def test_parse_trig(self):
    self.assertEqual(prs.parseTrig('cos(10)'), ['cos', '10'])

if __name__ == '__main__':
  unittest.main()