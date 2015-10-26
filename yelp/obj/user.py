# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class User(ResponseObject):

    _fields = [
        'id',
        'image_url',
        'name'
    ]

    def __init__(self, response):
        super(User, self).__init__(response)
