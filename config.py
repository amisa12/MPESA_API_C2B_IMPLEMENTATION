from __future__ import absolute_import

import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = True

    SECRET_KEY = 'This string will be replaced with a proper key in production.'
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user_name:db_password/database_name'
    SQLALCHEMY_POOL_SIZE = 20
    SQLALCHEMY_MAX_OVERFLOW = 0
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(DevelopmentConfig):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/mpesa_app'


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}