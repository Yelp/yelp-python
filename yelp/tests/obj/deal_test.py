# -*- coding: UTF-8 -*-
import json

from yelp.obj.deal import Deal


def test_init_deal():
    with open('json/business_response.json') as biz:
        response = json.load(biz)['deals'][0]
        deal = Deal(response)
        assert deal.url == response['url']
        assert len(deal.options) == len(response['options'])
