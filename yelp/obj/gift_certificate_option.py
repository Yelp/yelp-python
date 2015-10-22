# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class GiftCertificateOption(ResponseObject):

    _fields = [
        'price',
        'formatted_price'
    ]

    def __init__(self, response):
        super(GiftCertificateOption, self).__init__(response)
