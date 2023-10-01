class Config(object):
    """Base config"""
    SECRET_KEY='secret'
    TESTING=False
    SESSION_TYPE='filesystem'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

class TestConfig(Config):
    TESTING=True
    pass

config = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}

