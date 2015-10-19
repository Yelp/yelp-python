# -*- coding: UTF-8 -*-
import json

from yelp.obj.business import Business
from yelp.obj.location import Location


def test_init_business():
    with open('json/business_response.json') as biz:
        response = json.load(biz)
        business = Business(response)
        assert business.id == response['id']
        assert len(business.deals) == len(response['deals'])
        assert len(business.gift_certificates) == len(
            response['gift_certificates']
        )
        assert len(business.reviews) == len(response['reviews'])
        assert type(business.location) is Location
