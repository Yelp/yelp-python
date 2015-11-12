# -*- coding: UTF-8 -*-
from tests.integration.integration_test import IntegrationTest
from yelp.obj.search_response import SearchResponse


class TestPhoneSearchIntegration(IntegrationTest):

    int_vcr = IntegrationTest.int_vcr
    cassette_params = IntegrationTest.cassette_params

    @int_vcr.use_cassette(**cassette_params)
    def test_phone_search(self):
        phone = '+14158267000'
        resp = self.client.phone_search(phone)
        assert type(resp) is SearchResponse
        assert phone in resp.businesses[0].phone
