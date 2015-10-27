# -*- coding: UTF-8 -*-
from yelp.obj.business import Business
from yelp.obj.region import Region
from yelp.obj.response_object import ResponseObject


class SearchResponse(ResponseObject):

    _fields = [
        'total'
    ]

    def __init__(self, response):
        super(SearchResponse, self).__init__(response)

        self._parse('businesses', Business, response)
        self._parse('region', Region, response)
