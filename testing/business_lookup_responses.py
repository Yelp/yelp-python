# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import responses

from testing.util import read_json_file


YELP_SAN_FRANCISCO = responses.Response(
    method="GET",
    url="https://api.yelp.com/v3/businesses/yelp-san-francisco",
    json=read_json_file("business_lookup_yelp_san_francisco.json"),
    status=200,
)


SACRE_COEUR_PARIS = responses.Response(
    method="GET",
    url="https://api.yelp.com/v3/businesses/basilique-du-sacré-cœur-de-montmartre-paris-3",  # noqa: E501
    json=read_json_file("business_lookup_sacre_coeur_paris.json"),
    status=200,
)
