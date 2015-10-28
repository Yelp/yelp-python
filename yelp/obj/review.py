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

        self._parse('user', User, response)
        self._parse_main_response_body('rating', Rating, response)
