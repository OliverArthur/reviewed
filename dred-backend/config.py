#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Secret key for signing cookies
    SECRET_KEY = '\x12pOX\xc2W[\x05\xc71\xbc\x83m&\xef\xb4\t\x83\xe6(\xf9\x93\x7f\xdf'
    # Statement for enabling the development environment
    DEBUG = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    # CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    # CSRF_SESSION_KEY = "secret"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    # Statement for enabling the development environment
    DEBUG = True
    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'dred.db')


class TestingConfig(Config):
    # Statement for enabling the testing environment
    DEBUG = False
    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'dred-test.sqlite')


class ProductionConfig(Config):
    # Statement for enabling the production environment
    DEBUG = False
    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'dred.db')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
