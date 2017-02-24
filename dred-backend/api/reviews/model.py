# !/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from marshmallow import Schema, fields
from api import db


class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(150))
    review = db.Column(db.String(350), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    reviewed = db.Column(db.DateTime, default=datetime.utcnow)
    published = db.Column(db.Boolean, default=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product', backref='reviews', lazy='dynamic')

    def __repr__(self):
        # This is only for representation how you want to see products
        # information after query.
        return "<Reviews(id='%s', user_name='%s')" \
            "title='%s', review='%s', rating='%s', reviewed='%s')>" % (
                self.id,
                self.user_name,
                self.title,
                self.review,
                self.rating,
                self.reviewed
            )


class ReviewsSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_name = fields.String()
    title = fields.String()
    review = fields.String()
    rating = fields.Integer()
    reviewed = fields.DateTime()

    class Meta:
        type_ = 'review',
        model = Reviews
        fields = ("id", "user_name", "title", "review", "rating", "reviewed")
