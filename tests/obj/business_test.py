# -*- coding: UTF-8 -*-
import json

from yelp.obj.business import Business
from yelp.obj.business import Category


def test_init_business():
    with open('json/business_response.json') as biz:
        response = json.load(biz)
        business = Business(response)
        assert business.id == response['id']


def test_business_category_is_tuple():
    with open('json/business_response.json') as biz:
        response = json.load(biz)
        business = Business(response)
        assert type(business.categories[0]) is Category
        assert business.categories[0].name
        assert business.categories[0].alias
