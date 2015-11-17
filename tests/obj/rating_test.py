# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.rating import Rating


def test_init_review_rating():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['reviews'][0]
        rating = Rating(response)
        assert rating.rating == response['rating']
        assert rating.img_url == response['rating_image_url']


def test_init_business_rating():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)
        rating = Rating(response)
        assert rating.rating == response['rating']
        assert rating.img_url == response['rating_img_url']
