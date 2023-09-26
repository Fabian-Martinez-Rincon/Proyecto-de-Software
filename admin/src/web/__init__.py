from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

    @app.get('/')
    def home():
        return 'Hello, World!'
    
    return app