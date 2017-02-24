# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import make_response, jsonify


# Server errors
ERROR_500 = {
    "http_code": 500,
    "code": "test_stat",
    "message": "Internal server error."
}

ERROR_404 = {
    "http_code": 404,
    "code": "test_stat",
    "message": "Resource could not be found."
}

ERROR_400 = {
    "http_code": 400,
    "code": "test_stat",
    "message": "No input data provided."
}

ERROR_422 = {
    "http_code": 422,
    "code": "test_stat",
    "message": "Invalid input."
}

ERROR_409 = {
    "http_code": 409,
    "code": "test_stat",
    "message": "Already exists."
}

ERROR_999 = {
    "http_code": 999,
    "code": "test_stat",
    "message": "Missed parameters."
}

# Reviews responses
REVIEWS_CREATED_SUCCESSFULLY = {
    "http_code": 201,
    "code": "status",
    "message": "The reviews has been created successfully."
}

REVIEWS_FOUND_SUCCESSFULLY = {
    "http_code": 200,
    "code": "status",
    "message": "The reviews has been found successfully."
}

REVIEWS_UPDATED_SUCCESSFULLY = {
    "http_code": 201,
    "code": "status",
    "message": "The review has been updated successfully."
}

REVIEWS_DELETED_SUCCESSFULLY = {
    "http_code": 204,
    "code": "status",
    "message": "The reviews has been deleted successfully."
}


def api_response(http_code=0, code=None, message=None, value=None):
    my_dict = {}

    if code is not None:
        my_dict['code'] = code

    if message is not None:
        my_dict['message'] = message

    if value is not None:
        my_dict['value'] = value

    # return response
    return make_response(jsonify(my_dict), http_code)
