# !/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from sqlalchemy.exc import IntegrityError

import api.utils.responses as res
from api.reviews.model import Reviews, ReviewsSchema
from api.utils.responses import api_response
from api import db


def get_reviews():
    review_query = Reviews.query.all()
    review_schema = ReviewsSchema()

    if review_query is None:
        return api_response(
            http_code=res.ERROR_404['http_code'],
            message=res.ERROR_404['message']
        )
    else:
        return api_response(
            http_code=res.REVIEWS_FOUND_SUCCESSFULLY['http_code'],
            message=res.REVIEWS_FOUND_SUCCESSFULLY['message'],
            value=review_schema.dump(review_query, many=True).data

        )


def get_one_review(review_id):
    result = Reviews.query.filter_by(id=review_id).first()
    review_schema = ReviewsSchema()

    if result is None:
        return api_response(
            http_code=res.ERROR_404['http_code'],
            message=res.ERROR_404['message']
        )
    else:
        return api_response(
            http_code=res.REVIEWS_FOUND_SUCCESSFULLY['http_code'],
            message=res.REVIEWS_FOUND_SUCCESSFULLY['message'],
            value=review_schema.dump(result).data
        )


def add_reviews(user_name, title, review, rating, facebook,
                twitter, linkedin, published):
    try:
        reviews = Reviews(
            user_name=user_name,
            title=title,
            review=review,
            facebook=facebook,
            twitter=twitter,
            linkedin=linkedin,
            published=published
        )

        # add review to the session
        db.session.add(reviews)
        # commit session
        db.session.commit()
        # print review status
        return reviews

    except IntegrityError as why:
        # logging the error
        logging.warning(why)

        # Return error.
        return None
    
    except Exception as why:

        # Logging the generic errors.
        logging.warning(why)

        # Return error.
        return None
