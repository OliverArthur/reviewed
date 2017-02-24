#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from config import config_by_name

# Define the database object which is imported
# by modules and controllers
# pylint: disable=C0103
db = SQLAlchemy()
# Dev configuration
toolbar = DebugToolbarExtension()


def create_app(config_name):
    # Define the WSGI application object
    app = Flask(__name__)
    # Configurations
    app.config.from_object(config_by_name[config_name])
    # initialize the db
    db.init_app(app)
    # initialize the dev toolbar
    toolbar.init_app(app)

    return app
