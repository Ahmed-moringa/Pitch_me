import os

class Config:
    '''
    Describes the general configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # DATABASE_PASS = os.environ.get('DATABASE_PASS')
    # UPLOADED_PHOTOS_DEST = 'app/static/images'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/pitchme'
    
    # emails configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):

    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass

class TestConfig(Config):

    '''
    Test configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/pitchme_test'


class DevConfig(Config):

    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ahmed:dawnfm@localhost/pitchme'
    DEBUG = True
    


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}