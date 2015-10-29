# -*- coding: UTF-8 -*-
from yelp.obj.gift_certificate_option import GiftCertificateOption
from yelp.obj.response_object import ResponseObject


class GiftCertificate(ResponseObject):

    _fields = [
        'id',
        'url',
        'image_url',
        'currency_code',
        'unused_balances'
    ]

    def __init__(self, response):
        super(GiftCertificate, self).__init__(response)

        self._parse('options', GiftCertificateOption, response)
