# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject
from yelp.obj.user import User


class Review(ResponseObject):

    _fields = [
        'id',
        'excerpt',
        'time_created',
        'rating',
        'rating_image_url',
        'rating_image_small_url',
        'rating_image_large_url',
    ]

    def __init__(self, response):
        super(Review, self).__init__(response)

        self._parse('user', User, response)
