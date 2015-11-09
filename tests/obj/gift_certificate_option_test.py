# -*- coding: UTF-8 -*-
import json

from yelp.obj.gift_certificate_option import GiftCertificateOption


def test_init_deal():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['gift_certificates'][0]['options'][0]
        gift_certificate_option = GiftCertificateOption(response)
        assert gift_certificate_option.price == response['price']
