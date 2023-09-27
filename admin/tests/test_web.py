from web import create_app

app = create_app()

app.testing = True

cliente = app.test_client()

def test_home():
    response = cliente.get('/')
    assert response.status_code == 200
    assert "Hello, World!" in response.data.decode('utf-8')
