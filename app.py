"""App"""
from calculator import CalculadoraFinanceira


class Run:
    """Exemplo de uso"""
    capital = 8059.95
    parcelas = 15
    tx_juros = 0.057089
    calc = CalculadoraFinanceira(capital, tx_juros, parcelas)
    montante, juros = calc.calcular_juros_simples()
    print(montante)


if __name__ == '__main__':
    Run()
