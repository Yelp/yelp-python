# -*- coding: UTF-8 -*-
from yelp.obj.deal_option import DealOption


class Deal(object):

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
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

        self._parse_options(response)

    def _parse_options(self, response):
        if 'options' in response:
            options_list = []
            for opt in response['options']:
                options_list.append(DealOption(opt))
            self.options = options_list
        else:
            self.options = None
