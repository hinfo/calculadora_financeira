"""App"""
from flask import Flask
from flask import jsonify
from flask_swagger import swagger

from calculator import CalculadoraFinanceira

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"descricao": "API Finance Calculator"})


@app.route("/juros_simples/<capital>/<tx_juros>/<periodo>", methods=['GET'])
def juros_simples(capital, tx_juros, periodo):
    money = float(capital)
    tax = float(tx_juros)
    period = int(periodo)
    calc = CalculadoraFinanceira(money, tax, period)
    montante, juros = calc.calcular_juros_simples()

    return jsonify({"montante": montante, "juros": juros})


@app.route("/juros_compostos/<capital>/<tx_juros>/<periodo>", methods=['GET'])
def jusros_compostos(capital, tx_juros, periodo):
    money = float(capital)
    tax = float(tx_juros)
    period = int(periodo)
    calc = CalculadoraFinanceira(money, tax, period)
    montante, juros = calc.calcular_juros_compostos()

    return jsonify({"montante": montante, "juros": juros})


@app.route("/spec")
def spec():
    """Interface para o swagger"""
    definitions = "capital: float, tx_juros: float, periodo: int"
    swag = swagger(app)
    swag['definitions'] = definitions
    swag['paths'] = ["/juros_simples/<capital>/<tx_juros>/periodo",
                     "/juros_compostos/<capital>/<tx_juros>/periodo"]
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "API Calculator"

    return jsonify(swag)


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
