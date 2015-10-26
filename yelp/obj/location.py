# -*- coding: UTF-8 -*-
from yelp.obj.coordinate import Coordinate
from yelp.obj.response_object import ResponseObject


class Location(ResponseObject):

    _fields = [
        'address',
        'city',
        'country_code',
        'cross_streets',
        'display_address',
        'geo_accuracy',
        'neighborhoods',
        'postal_code',
        'state_code'
    ]

    def __init__(self, response):
        super(Location, self).__init__(response)

        self._parse('coordinate', Coordinate, response)
