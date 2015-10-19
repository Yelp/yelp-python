# -*- coding: UTF-8 -*-


class GiftCertificateOption(object):

    _fields = [
        'price',
        'formatted_price'
    ]

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)
