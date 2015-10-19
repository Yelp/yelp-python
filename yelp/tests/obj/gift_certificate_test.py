# -*- coding: UTF-8 -*-
import json

from yelp.obj.gift_certificate import GiftCertificate


def test_init_gift_certificate():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['gift_certificates'][0]
        gift_certificate = GiftCertificate(response)
        assert gift_certificate.id == response['id']
        assert len(gift_certificate.options) == len(response['options'])
