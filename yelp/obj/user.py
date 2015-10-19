# -*- coding: UTF-8 -*-


class User(object):

    _fields = [
        'id',
        'image_url',
        'name'
    ]

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)
