from urllib import quote_plus
import os


class HardCoded(object):
    """Constants used throughout the application.

    All hard coded settings/data that are not actual/official configuration options for Flask, Celery, or their
    extensions goes here.
    """
    ADMINS = ['me@me.test']
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ENVIRONMENT = property(lambda self: self.__class__.__name__)
    MAIL_EXCEPTION_THROTTLE = 24 * 60 * 60
    _SQLALCHEMY_DATABASE_DATABASE = 'pypi_portal'
    _SQLALCHEMY_DATABASE_HOSTNAME = 'localhost'
    _SQLALCHEMY_DATABASE_PASSWORD = 'pypi_p@ssword'
    _SQLALCHEMY_DATABASE_USERNAME = 'pypi_service'

class Config(Config):
    """Default Flask configuration inherited by all environments. Use this for development environments."""
    DEBUG = True
    TESTING = False
    SECRET_KEY = "i_don't_want_my_cookies_expiring_while_developing"
    MAIL_SERVER = 'smtp.localhost.test'
    MAIL_DEFAULT_SENDER = 'admin@demo.test'
    MAIL_SUPPRESS_SEND = True
    REDIS_URL = 'redis://localhost/0'
    SQLALCHEMY_DATABASE_URI = property(lambda self: 'mysql://{u}:{p}@{h}/{d}'.format(
        d=quote_plus(self._SQLALCHEMY_DATABASE_DATABASE), h=quote_plus(self._SQLALCHEMY_DATABASE_HOSTNAME),
        p=quote_plus(self._SQLALCHEMY_DATABASE_PASSWORD), u=quote_plus(self._SQLALCHEMY_DATABASE_USERNAME)
    ))


class Testing(Config):
    TESTING = True
    CELERY_ALWAYS_EAGER = True
    REDIS_URL = 'redis://localhost/1'
    _SQLALCHEMY_DATABASE_DATABASE = 'pypi_portal_testing'


class Production(Config):
    DEBUG = False
    SECRET_KEY = None  # To be overwritten by a YAML file.
    ADMINS = ['my-team@me.test']
    MAIL_SUPPRESS_SEND = False
    STATICS_MINIFY = True
