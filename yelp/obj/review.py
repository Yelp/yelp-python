# -*- coding: UTF-8 -*-
from yelp.obj.rating import Rating
from yelp.obj.user import User


class Review(object):

    _fields = [
        'id',
        'excerpt',
        'time_created'
    ]

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

        self._parse_rating(response)
        self._parse_user(response)

    def _parse_rating(self, response):
        if 'rating' in response:
            self.rating = Rating(response)
        else:
            self.rating = None

    def _parse_user(self, response):
        if 'user' in response:
            self.user = User(response['user'])
        else:
            self.user = None
