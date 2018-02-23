import os

#Parent configuration class.
class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    #is a random string of characters that's used to generate hashes
    SECRET = os.getenv('SECRET')
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

#Configurations for Development
class DevelopmentConfig(Config):
    #tells the app to run under debugging mode with the flask Debugger
    DEBUG = True

#Configurations for Staging.
class StagingConfig(Config):
    DEBUG = True

#Configurations for Production.
class ProductionConfig(Config): 
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
