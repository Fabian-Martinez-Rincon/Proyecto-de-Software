from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    """
    Inicializacion de la aplicacion
    """
    db.init_app(app)
    config_db(app)

def config_db(app):
    """
    Configuracion de la aplicacion
    """
    @app.teardown_request
    def close_session(exception=None):
        db.session.close()

def reset_database():
    """
    Reinicia la base de datos
    """
    print('Holaaaaa')
    db.drop_all()
    db.create_all()

