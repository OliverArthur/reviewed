#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from flask import request, jsonify
import api.utils.responses as res
from api.utils.responses import api_response
from api.reviews import reviews
from api.reviews.model import Reviews, ReviewsSchema
from api.reviews import controller

@reviews.route('/review', methods=['POST'])
def add_new_review():
    try:
        # Get inputs data
        json_dict = request.get_json()

        user_name = json_dict['user_name']
        title = json_dict['title']
        review = json_dict['review']
        rating = json_dict['rating']
        facebook = json_dict['facebook']
        twitter = json_dict['twitter']
        linkedin = json_dict['linkedin']
        published = json_dict['published']

    except Exception as why:
        # Logging the error
        logging.warning(why)

        return api_response(
            # Return missed parameter error.
            http_code=res.ERROR_999['http_code'],
            message=res.ERROR_999['message'],
            code=res.ERROR_999['code']
        )

    new_review = controller.add_reviews(
        user_name=user_name,
        title=title,
        review=review,
        rating=rating,
        facebook=facebook,
        twitter=twitter,
        linkedin=linkedin,
        published=published
    )

    # Reviews schema for some fields.
    reviews_schema = ReviewsSchema(only=(
        'id',
        'user_name',
        'title',
        'review',
        'rating',
        'facebook',
        'twitter',
        'linkedin',
        'published',
        'reviewed')
    )
    # Return item created.
    return api_response(
        http_code=res.REVIEW_CREATED_SUCCESSFULLY['http_code'],
        message=res.REVIEW_CREATED_SUCCESSFULLY['message'],
        value=reviews_schema.dump(new_review).data
    )


@reviews.route('/all/reviews', methods=['GET'])
def get_all_products():
    get_reviews_schema = ReviewsSchema()
    data_dicts = get_reviews_schema.dump(
        controller.get_reviews, many=True).data

    return jsonify(data_dicts)


@reviews.route('/<review_id>', methods=['GET'])
def get_review_by_id(review_id):

    data_response = ReviewsSchema.dump(
        controller.get_one_review(review_id)).data

    return jsonify(data_response)
