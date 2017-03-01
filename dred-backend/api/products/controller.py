# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from sqlalchemy.exc import IntegrityError

import api.utils.responses as res
from api.utils.responses import api_response
from api.products.model import Product, ProductSchema
from api import db


def create_products(product, product_type):

    try:
        products = Product(
            product=product,
            product_type=product_type
        )

        # add product to the session
        db.session.add(products)
        # commit session
        db.session.commit()
        # print product status
        return products

    except IntegrityError as why:
        # loggin the error
        logging.warning(why)

        # Return none if there is product unique constraint error.
        return None

    except Exception as why:

        # Logging the generic errors.
        logging.warning(why)

        # Return error.
        return None


def get_product():
    pruduct_query = Product.query.all()
    pruduct_schema = ProductSchema()

    if pruduct_query is None:
        return api_response(
            http_code=res.ERROR_404['http_code'],
            message=res.ERROR_404['message']
        )
    else:
        return api_response(
            http_code=res.REVIEW_FOUND_SUCCESSFULLY['http_code'],
            message=res.REVIEW_FOUND_SUCCESSFULLY['message'],
            value=pruduct_schema.dump(pruduct_query, many=True).data

        )
