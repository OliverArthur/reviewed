# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from flask import request, jsonify
import api.utils.responses as res
from api.utils.responses import api_response
from api.products import prod
from api.products.model import Product, ProductSchema
from api.products import controller


@prod.route('/add/product', methods=['POST'])
def add_new_product():
    try:
        # Get inputs data
        json_dict = request.get_json()

        product = json_dict['product']

    except Exception as why:
        # Logging the error
        logging.warning(why)

        return api_response(
            # Return missed parameter error.
            http_code=res.ERROR_999['http_code'],
            message=res.ERROR_999['message'],
            code=res.ERROR_999['code']
        )

    new_product = controller.create_products(product=product)

    # Products schema for some fields.
    products_schema = ProductSchema(only=('id', 'product',))

    # Return item created.
    return api_response(
        http_code=res.PRODUCT_CREATED_SUCCESSFULLY['http_code'],
        message=res.PRODUCT_CREATED_SUCCESSFULLY['message'],
        value=products_schema.dump(new_product).data
    )


@prod.route('/all', methods=['GET'])
def get_all_products():
    get_products_schema = ProductsSchema()
    data_dicts = get_products_schema.dump(
        service.get_products(), many=True).data

    return jsonify(data_dicts)


@prod.route('/get/<product_id>', methods=['GET'])
def get_product_by_id(product_id):

    data_response = ProductsSchema.dump(
        service.get_one_product(product_id)).data

    return jsonify(data_response)
