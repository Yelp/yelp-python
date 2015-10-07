# -*- coding: UTF-8 -*-
import json

from yelp.obj.business import Business


def test_init_business():
    with open('json/business_response.json') as biz:
        response = json.load(biz)
        business = Business(response)
        assert business.id == response['id']  # "flour-water-san-francisco"
        assert len(business.reviews) == len(response['reviews'])
