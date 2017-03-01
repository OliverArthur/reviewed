#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from config import config_by_name
from flask_cors import CORS, cross_origin
# Define the database object which is imported
# by modules and controllers
# pylint: disable=C0103
db = SQLAlchemy()
# Dev configuration
toolbar = DebugToolbarExtension()

cors = CORS()


def create_app(config_name):
    # Define the WSGI application object
    app = Flask(__name__)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    # Configurations
    app.config.from_object(config_by_name[config_name])
    # initialize the db
    db.init_app(app)
    # initialize the dev toolbar
    toolbar.init_app(app)

    from api.reviews import reviews as reviews_blueprint
    app.register_blueprint(reviews_blueprint, url_prefix='/api/v1')

    from api.products import prod as prod_blueprint
    app.register_blueprint(prod_blueprint, url_prefix='/api/v1')
    
    return app
