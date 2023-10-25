class Config(object):
    """Base config"""
    SECRET_KEY='secret'
    TESTING=False
    SESSION_TYPE='filesystem'

class ProdConfig(Config):
    pass

class DevConfig(Config):

    DB_USER = "postgres"
    DB_PASSWORD = "postgres"
    DB_HOST = "localhost"
    DB_NAME = "proyecto"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
        )
    

class TestConfig(Config):
    TESTING=True
    pass

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}

