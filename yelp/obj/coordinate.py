# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class Coordinate(ResponseObject):

    _fields = [
        'latitude',
        'longitude'
    ]

    def __init__(self, response):
        super(Coordinate, self).__init__(response)
