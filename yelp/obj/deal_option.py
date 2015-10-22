# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class DealOption(ResponseObject):

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
        super(DealOption, self).__init__(response)
