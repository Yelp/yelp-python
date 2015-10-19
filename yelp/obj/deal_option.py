# -*- coding: UTF-8 -*-


class DealOption(object):

    _fields = [
        'title',
        'purchase_url',
        'price',
        'formatted_price',
        'original_price',
        'formatted_original_price',
        'is_quantity_limited',
        'remaining_count'
    ]

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)
