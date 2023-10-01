from tests import cliente

def test_home():
    response = cliente.get('/')
    assert response.status_code == 200
    assert "Hello, World!" in response.data.decode('utf-8')
