# -*- coding: UTF-8 -*-
import json

from yelp.obj.rating import Rating


def test_init_rating():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['reviews'][0]
        rating = Rating(response)
        assert rating.rating == response['rating']
        assert rating.img_url == response['rating_image_url']
