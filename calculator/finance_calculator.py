"""App calculadora financeira"""
from math import pow


class CalculadoraFinanceira:
    """Calculadora Financeira"""

    def __init__(self, capital_inicial=None, taxa_juros=None, periodo=None):
        self.capital = capital_inicial
        self.taxa_juros = taxa_juros
        self.periodo = periodo

    def calcular_coeficiente(self):
        """Calcula o coeficiente de emprestimo"""
        coeficiente = \
            self.taxa_juros / (1 - pow(1 + self.taxa_juros, - self.periodo))
        return coeficiente

    def calcular_juros_simples(self):
        """Calcula o montante com base em juros simples"""
        juros_simples = self.capital * self.taxa_juros * self.periodo
        montante = self.capital + juros_simples
        return montante, juros_simples

    def calcular_juros_compostos(self):
        """Calcula o montante com base em juros compostos"""
        juros_compostos = self.capital * pow(1 + self.taxa_juros, self.periodo)
        montante_resultante = self.capital + juros_compostos
        return montante_resultante, juros_compostos
