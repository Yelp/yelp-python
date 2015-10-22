# -*- coding: UTF-8 -*-
from yelp.obj.rating import Rating
from yelp.obj.response_object import ResponseObject
from yelp.obj.user import User


class Review(ResponseObject):

    _fields = [
        'id',
        'excerpt',
        'time_created'
    ]

    def __init__(self, response):
        super(Review, self).__init__(response)

        self._parse_one_to_object('user', User, response)
        self._parse_rating(response)

    def _parse_rating(self, response):
        self.rating = Rating(response) if 'rating' in response else None
