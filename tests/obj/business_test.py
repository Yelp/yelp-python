# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.business import Business
from yelp.obj.business import Category


def test_init_business():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)
        business = Business(response)
        assert business.id == response['id']


def test_business_category_is_tuple():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)
        business = Business(response)
        assert type(business.categories[0]) is Category
        assert business.categories[0].name == "Indian"
        assert business.categories[0].alias == "indpak"
