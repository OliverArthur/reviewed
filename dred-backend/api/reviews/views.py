#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from flask import request, jsonify
import api.utils.responses as res
from api.utils.responses import api_response
from api.reviews import reviews
from api.reviews.model import ReviewsSchema
from api.reviews import controller
