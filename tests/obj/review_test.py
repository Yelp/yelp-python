# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.review import Review
from yelp.obj.user import User


def test_init_review():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['reviews'][0]
        review = Review(response)
        assert review.id == response['id']
        assert type(review.user) is User
