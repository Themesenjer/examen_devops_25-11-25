import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Verifica que la página principal cargue correctamente"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Liga Pro" in rv.data

def test_api_tabla(client):
    """Verifica que la API devuelva datos"""
    rv = client.get('/api/tabla')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert len(json_data) > 0