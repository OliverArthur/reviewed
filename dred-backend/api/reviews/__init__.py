#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

reviews = Blueprint('reviews', __name__)

from api.reviews import views
