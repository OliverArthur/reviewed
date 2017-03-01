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
        product_type = json_dict['product_type']

    except Exception as why:
        # Logging the error
        logging.warning(why)

        return api_response(
            # Return missed parameter error.
            http_code=res.ERROR_999['http_code'],
            message=res.ERROR_999['message'],
            code=res.ERROR_999['code']
        )

    new_product = controller.create_products(product=product, product_type=product_type)

    # Products schema for some fields.
    products_schema = ProductSchema(only=('id', 'product', 'product_type'))

    # Return item created.
    return api_response(
        http_code=res.PRODUCT_CREATED_SUCCESSFULLY['http_code'],
        message=res.PRODUCT_CREATED_SUCCESSFULLY['message'],
        value=products_schema.dump(new_product).data
    )


@prod.route('/all/products', methods=['GET'])
def get_all_products():
    get_products_schema = ProductSchema()
    data_dicts = get_products_schema.dump(
        controller.get_products(), many=True).data

    return jsonify(data_dicts)


@prod.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):

    result = Product.query.filter_by(id=product_id).first()
    product_schema = ProductSchema()

    if result is None:
        return api_response(
            http_code=res.ERROR_404['http_code'],
            message=res.ERROR_404['message']
        )
    else:
        return api_response(
            http_code=res.REVIEW_FOUND_SUCCESSFULLY['http_code'],
            message=res.REVIEW_FOUND_SUCCESSFULLY['message'],
            value=product_schema.dump(result).data
        )
