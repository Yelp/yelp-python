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
