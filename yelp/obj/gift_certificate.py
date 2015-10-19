# -*- coding: UTF-8 -*-
from yelp.obj.gift_certificate_option import GiftCertificateOption


class GiftCertificate(object):

    _fields = [
        'id',
        'url',
        'image_url',
        'currency_code',
        'unused_balances'
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
                options_list.append(GiftCertificateOption(opt))
            self.options = options_list
        else:
            self.options = None
