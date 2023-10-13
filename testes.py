import unittest
from converter import fahrenheit_para_celsius, celsius_para_fahrenheit

def test_conversao_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100
    assert fahrenheit_para_celsius(68) == 20

def test_conversao_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(20) == 68

def run_tests():
    test_conversao_fahrenheit_para_celsius()
    test_conversao_celsius_para_fahrenheit()
    print("Todos os testes passaram com sucesso!")

run_tests()