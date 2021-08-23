"""
Application Configuration
"""
# ==============================================================================


class DevConfig:
    # Statement for enabling the development environment
    VERSION = "0.0.1"
    DEBUG = True

    DB_HOST = 'localhost'
    DB_DATABASE = 'gino'


class QAConfig:
    # Statement for enabling the development environment
    VERSION = "0.0.1"
    DEBUG = True

    DB_HOST = 'localhost'
    DB_DATABASE = 'gino'


class ProdConfig:
    # Statement for enabling the development environment
    VERSION = "0.0.1"
    DEBUG = False

    DB_HOST = 'localhost'
    DB_DATABASE = 'gino'
