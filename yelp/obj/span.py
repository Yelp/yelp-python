# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class Span(ResponseObject):

    _fields = [
        'latitude_delta',
        'longitude_delta'
    ]
