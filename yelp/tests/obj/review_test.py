# -*- coding: UTF-8 -*-
import json

from yelp.obj.rating import Rating
from yelp.obj.review import Review


def test_init_review():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['reviews'][0]
        review = Review(response)
        assert review.id == response['id']
        assert type(review.rating) is Rating
