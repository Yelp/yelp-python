# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.user import User


def test_init_user():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['reviews'][0]['user']
        user = User(response)
        assert user.id == response['id']
        assert user.image_url == response['image_url']
        assert user.name == response['name']
