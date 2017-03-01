# !/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from marshmallow import Schema, fields
from api import db

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(150), nullable=False)
    product_type = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        # This is only for representation how you want to see products
        # information after query.
        return "<Product(id='%s', product='%s', product_type='%s')>" % (
                self.id,
                self.product,
                self.product_type
            )


class ProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    product = fields.String()
    product_type = fields.String()

    class Meta:
        type_ = 'product',
        model = Product
        fields = ("id", "product")
