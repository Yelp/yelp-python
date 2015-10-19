# -*- coding: UTF-8 -*-
from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['latitude', 'longitude'])


class Location(object):

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
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

        self.coordinate = Coordinate(
            response['coordinate']['latitude'],
            response['coordinate']['longitude']
        )
