from fastapi import FastAPI
import uvicorn

from .calculator import CalculadoraFinanceira

app = FastAPI()


@app.get("/")
async def home():
    return {"descricao": "API Finance Calculator"}


@app.get("/juros_simples/{capital}/{tx_juros}/{periodo}")
async def juros_simples(capital, tx_juros, periodo):
    money = float(capital)
    tax = float(tx_juros)
    period = int(periodo)
    calc = CalculadoraFinanceira(money, tax, period)
    montante, juros = calc.calcular_juros_simples()

    return {"montante": montante, "juros": juros}


@app.get("/juros_compostos/{capital}/{tx_juros}/{periodo}")
async def jusros_compostos(capital, tx_juros, periodo):
    money = float(capital)
    tax = float(tx_juros)
    period = int(periodo)
    calc = CalculadoraFinanceira(money, tax, period)
    montante, juros = calc.calcular_juros_compostos()

    return {"montante": montante, "juros": juros}



if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
