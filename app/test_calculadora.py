import pytest

from . import calculadora


# Calculadora


# Operador invalido
def test_calculadora_operador_invalido():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, 6, "teste") is False


# Numero invalido
def test_calculadora_numero_invalido():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, "teste", "adicao") is False


# OPERADORES


# Adicao
def test_operacao_adicao():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, 6, "adicao") == 12


# Subtracao
def test_operacao_subtracao():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, 6, "subtracao") == 0


# Divisao
def test_operacao_divisao():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, 6, "divisao") == 1


# Divisao por zero
def test_operacao_divisao_zero():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, 0, "divisao") is False


# Multiplicacao
def test_operacao_multiplicacao():
    calc = calculadora.Calculadora()
    assert calc.calcular(6, 6, "multiplicacao") == 36
