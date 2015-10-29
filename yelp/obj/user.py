# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class User(ResponseObject):

    _fields = [
        'id',  # access as user.user_id
        'image_url',
        'name'
    ]
