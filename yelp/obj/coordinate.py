# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class Coordinate(ResponseObject):

    _fields = [
        'latitude',
        'longitude'
    ]
