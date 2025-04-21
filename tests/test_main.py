from ..app.main import app
from fastapi.testclient import TestClient

from unittest import TestCase

client = TestClient(app)

class TestMain(TestCase):
    def test_app(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"descricao": "API Finance Calculator"}
    
    def test_juros_simples(self):
        response = client.get("/juros_simples/8059.95/0.05/15")
        assert response.status_code == 200
        assert response.json() == {"montante": 14104.912499999999, "juros": 6044.9625}

    def test_juros_compostos(self):
        response = client.get("/juros_compostos/8059.95/0.05/15")
        assert response.status_code == 200
        assert response.json() == {"montante": 24816.007179646662, "juros": 16756.05717964666}