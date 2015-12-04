# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.business import Business
from yelp.obj.deal import Deal
from yelp.obj.location import Location
from yelp.obj.response_object import ResponseObject


class TestResponseObject(object):

    @classmethod
    def setup_class(cls):
        with io.open(resource_filename('json/business_response.json')) as resp:
            cls.response = json.load(resp)

    def test_response_obj_sets_correct_fields(self):
        with io.open(resource_filename('json/test_response.json')) as resp:
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

    def test_parse_main_response_body(self):
        obj = ResponseObject('{}')
        obj._parse_main_response_body('business', Business, self.response)
        assert type(obj.business) is Business
