#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

prod = Blueprint('prod', __name__)

from api.products import views
