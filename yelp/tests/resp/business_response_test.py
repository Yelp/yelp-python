# -*- coding: UTF-8 -*-
from yelp.obj.business import Business
from yelp.resp.business_response import BusinessResponse


def test_make_business_response():
    biz_response = BusinessResponse({})
    assert biz_response.response == {}
    assert type(biz_response.business) is Business
