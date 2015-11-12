# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.deal_option import DealOption


def test_init_deal_option():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['deals'][0]['options'][0]
        deal_option = DealOption(response)
        assert deal_option.purchase_url == response['purchase_url']
