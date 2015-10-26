# -*- coding: UTF-8 -*-
from yelp.obj.deal_option import DealOption
from yelp.obj.response_object import ResponseObject


class Deal(ResponseObject):

    _fields = [
        'id',
        'title',
        'url',
        'image_url',
        'currency_code',
        'time_start',
        'time_end',
        'is_popular',
        'what_you_get',
        'important_restriction',
        'additional_restrictions'
    ]

    def __init__(self, response):
        super(Deal, self).__init__(response)

        self._parse('options', DealOption, response)
