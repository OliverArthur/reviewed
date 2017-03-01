# !/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from marshmallow import Schema, fields
from api import db

reviews = db.Table('reviews_product', 
    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
    db.Column('reviews_id', db.Integer, db.ForeignKey('reviews.id'))
)

class Reviews(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(150))
    review = db.Column(db.String(350), nullable=False)
    rating = db.Column(db.Integer)
    facebook = db.Column(db.Boolean, default=False)
    twitter = db.Column(db.Boolean, default=False)
    linkedin = db.Column(db.Boolean, default=False)
    published = db.Column(db.Boolean, default=False)
    reviewed = db.Column(db.DateTime, default=datetime.utcnow)
    _reviews = db.relationship('Product', secondary=reviews, lazy='joined',
                                backref=db.backref('reviews', lazy='dynamic'))

    def __repr__(self):
        # This is only for representation how you want to see products
        # information after query.
        return "<Reviews(id='%s', user_name='%s')" \
            "title='%s', review='%s', rating='%s', facebook='%s', twitter='%s')" \
            "linkedin='%s', published='%s', reviewed='%s'>" % (
                self.id,
                self.user_name,
                self.title,
                self.review,
                self.rating,
                self.facebook,
                self.twitter,
                self.linkedin,
                self.published,
                self.reviewed
            )


class ReviewsSchema(Schema):
    id = fields.Integer(dump_only=True)
    user_name = fields.String()
    title = fields.String()
    review = fields.String()
    rating = fields.Integer()
    facebook = fields.Boolean()
    twitter = fields.Boolean()
    linkedin = fields.Boolean()
    published = fields.Boolean()
    reviewed = fields.DateTime()

    class Meta:
        type_ = 'reviews',
        model = Reviews
        fields = (
            "id", "user_name", "title", "review", 
            "rating", "facebook", "twitter", "linkedin",
            "published", "reviewed"
        )
