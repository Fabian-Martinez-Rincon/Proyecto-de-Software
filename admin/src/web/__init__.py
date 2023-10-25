from flask import Flask
from flask import render_template
from src.core import database
from src.web.config import config
from src.web.controllers.issues import issues_bp

def create_app(env='dev', static_folder='../../static'):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    database.init_app(app)

    app.register_blueprint(issues_bp)

    @app.get('/')
    def home():
        return render_template('home.html')
        
    @app.get('/about')
    def about():
        return render_template('about.html')
    
    @app.get('/contact')
    def contact():
        return render_template('contact.html')
    
    @app.get('/consultas')
    def ussues():
        return render_template('issues/index.html')
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error_code='404', error_message='Página no encontrada'), 404


    @app.cli.command(name='resetdb')
    def resetdb():
        """
        Comando para reiniciar la base de datos
        """
        print('Holaaaa')
        #database.reset_database()
        
    return app
