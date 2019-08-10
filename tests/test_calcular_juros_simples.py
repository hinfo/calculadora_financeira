"""Testes"""
from unittest import TestCase

from calculator import CalculadoraFinanceira


class CalculadoraTest(TestCase):
    """Classe de testes"""

    def test_calcular_juros_simples(self):
        """Teste juros simples"""
        capital = 8059.95
        periodo = 15
        tx_juros = 0.057089
        calc = CalculadoraFinanceira(capital, tx_juros, periodo)
        montante, juros = calc.calcular_juros_simples()
        self.assertEqual(round(montante, 2), 14961.97)
        self.assertEqual(round(juros, 2), 6902.02)

    def test_calcular_juros_compostos(self):
        """Teste para calcular juros compostos"""
        capital = 8059.95
        periodo = 15
        tx_juros = 0.057089
        calc = CalculadoraFinanceira(capital, tx_juros, periodo)
        montante, juros = calc.calcular_juros_compostos()
        self.assertEqual(round(montante, 2), 26595.51)
        self.assertEqual(round(juros, 2), 18535.56)

    def test_calcular_coeficiente(self):
        """Teste para obter o coeficiente de financiamento"""
        periodo = 15
        tx_juros = 0.057089
        calc = CalculadoraFinanceira(None, tx_juros, periodo)
        coeficiente = calc.calcular_coeficiente()
        self.assertEqual(round(coeficiente, 6), 0.101013)
