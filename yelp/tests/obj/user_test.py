# -*- coding: UTF-8 -*-
import json

from yelp.obj.user import User


def test_init_user():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['reviews'][0]['user']
        user = User(response)
        assert user.user_id == response['id']
        assert user.image_url == response['image_url']
        assert user.name == response['name']
