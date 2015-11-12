# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.obj.deal import Deal


def test_init_deal():
    with io.open(resource_filename('json/business_response.json')) as biz:
        response = json.load(biz)['deals'][0]
        deal = Deal(response)
        assert deal.url == response['url']
