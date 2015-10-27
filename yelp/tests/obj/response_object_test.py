# -*- coding: UTF-8 -*-
import json

from yelp.obj.deal import Deal
from yelp.obj.location import Location
from yelp.obj.rating import Rating
from yelp.obj.response_object import ResponseObject


class TestResponseObject(object):

    @classmethod
    def setup_class(cls):
        with open('json/business_response.json') as resp:
            cls.response = json.load(resp)

    def test_response_obj_sets_correct_fields(self):
        with open('json/test_response.json') as resp:
            response = json.load(resp)
        obj = ResponseObject('{}')
        obj._fields = ['id', 'name']
        obj.__init__(response)
        assert obj.id == response['id']
        assert obj.name == response['name']
        assert hasattr(obj, 'do_not_display') is False

    def test_response_obj_parse_list(self):
        obj = ResponseObject('{}')
        obj._parse('deals', Deal, self.response)
        assert len(obj.deals) == len(self.response['deals'])
        assert type(obj.deals[0]) is Deal

    def test_response_obj_parse_one(self):
        obj = ResponseObject('{}')
        obj._parse('location', Location, self.response)
        assert type(obj.location) is Location

    def test_parse_main_response(self):
        obj = ResponseObject('{}')
        obj._parse_main_response('rating', Rating, self.response)
        assert type(obj.rating) is Rating
