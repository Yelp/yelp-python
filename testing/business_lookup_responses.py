# -*- coding: utf-8 -*-
import responses
from testing.util import read_json_file


BUSINESS_LOOKUP_RESPONSE = responses.Response(
    method="GET",
    url="https://api.yelp.com/v3/businesses/yelp-san-francisco",
    json=read_json_file("business_lookup_yelp_san_francisco.json"),
    status=200,
)
