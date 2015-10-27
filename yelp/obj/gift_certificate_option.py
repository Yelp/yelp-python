# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class GiftCertificateOption(ResponseObject):

    _fields = [
        'price',
        'formatted_price'
    ]
