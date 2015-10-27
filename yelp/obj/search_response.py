# -*- coding: UTF-8 -*-
from yelp.obj.business import Business
from yelp.obj.response_object import ResponseObject


class SearchResponse(ResponseObject):

    _fields = [
        'total'
    ]

    def __init__(self, response):
        super(SearchResponse, self).__init__(response)

        self._parse('businesses', Business, response)
