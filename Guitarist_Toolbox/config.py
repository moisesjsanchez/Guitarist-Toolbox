import os
from Guitarist_Toolbox.var import my_postgres


class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = my_postgres
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class TestConfig(BaseConfig):
    TESTING = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
