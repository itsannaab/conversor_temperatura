import unittest
from converter import fahrenheit_para_celsius, celsius_para_fahrenheit

class TestConversorTemperatura(unittest.TestCase):
    def test_conversao_fahrenheit_para_celsius(self):
        self.assertEqual(fahrenheit_para_celsius(32), 0)
        self.assertEqual(fahrenheit_para_celsius(212), 0)
        self.assertEqual(fahrenheit_para_celsius(68), 20)

    def test_conversao_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)
        self.assertEqual(celsius_para_fahrenheit(100), 212)
        self.assertEqual(celsius_para_fahrenheit(20), 68)

if __name__ == '__main__':
    unittest.main()