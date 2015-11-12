# -*- coding: UTF-8 -*-
import json

from tests.testing import resource_filename
from yelp.obj.gift_certificate_option import GiftCertificateOption


def test_init_gift_certificate_option():
    with open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['gift_certificates'][0]['options'][0]
        gift_certificate_option = GiftCertificateOption(response)
        assert gift_certificate_option.price == response['price']
