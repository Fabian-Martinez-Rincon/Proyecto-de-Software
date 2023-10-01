from web import create_app

app = create_app(env='test')
cliente = app.test_client()
