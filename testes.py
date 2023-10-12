import unittest
from converter import Conversor

class TestConversorKelvin(unittest.TestCase):

    def setUp(self):
        self.conversor_test = Conversor('K', 300)

    def test_convertendo_de_kelvin_para_celsius(self):
        self.conversor_test.converter('C')

        self.assertEqual(self.conversor_test.get_temp().get_escala(), 'C')
        self.assertEqual(self.conversor_test.get_temp().get_temperatura(), 27.00)

    def test_convertendo_de_kelvin_para_fahrenheit(self):
        self.conversor_test.converter('F')

        self.assertEqual(self.conversor_test.get_temp().get_escala(), 'F')
        self.assertEqual(self.conversor_test.get_temp().get_temperatura(), 80.60)

if __name__ == '__main__':
    unittest.main()





