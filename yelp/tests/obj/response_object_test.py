# -*- coding: UTF-8 -*-
import json

from yelp.obj.deal import Deal
from yelp.obj.location import Location
from yelp.obj.response_object import ResponseObject


def test_response_parse_list():
    with open('json/business_response.json') as resp:
        response = json.load(resp)
    obj = ResponseObject('{}')
    obj._parse('deals', Deal, response)
    assert len(obj.deals) == len(response['deals'])
    assert type(obj.deals[0]) is Deal


def test_response_parse_one():
    with open('json/business_response.json') as resp:
        response = json.load(resp)
    obj = ResponseObject('{}')
    obj._parse('location', Location, response)
    assert type(obj.location) is Location
