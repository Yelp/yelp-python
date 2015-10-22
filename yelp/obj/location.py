# -*- coding: UTF-8 -*-
from collections import namedtuple
from yelp.obj.response_object import ResponseObject

Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])


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

        if 'coordinate' in response:
            self.coordinate = Coordinate(
                response['coordinate']['latitude'],
                response['coordinate']['longitude']
            )
        else:
            self.coordinate = None
