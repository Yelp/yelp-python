# -*- coding: UTF-8 -*-
from yelp.obj.business import Business
from yelp.obj.business_response import BusinessResponse


def test_make_business_response():
    biz_response = BusinessResponse({})
    assert type(biz_response.business) is Business
