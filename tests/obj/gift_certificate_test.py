# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.gift_certificate import GiftCertificate


def test_init_gift_certificate():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['gift_certificates'][0]
        gift_certificate = GiftCertificate(response)
        assert gift_certificate.id == response['id']
