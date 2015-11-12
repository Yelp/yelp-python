# -*- coding: UTF-8 -*-
import pytest

from tests.integration.integration_test import IntegrationTest
from yelp.errors import BusinessUnavailable
from yelp.errors import MissingParameter
from yelp.obj.business_response import BusinessResponse


class TestBusinessIntegration(IntegrationTest):

    int_vcr = IntegrationTest.int_vcr
    cassette_params = IntegrationTest.cassette_params

    @int_vcr.use_cassette(**cassette_params)
    def test_url_with_no_params(self):
        with pytest.raises(MissingParameter):
            self.client.get_business('')

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_returns_correct_result(self):
        business_id = "yelp-san-francisco"
        resp = self.client.get_business(business_id)
        assert type(resp) is BusinessResponse
        assert resp.business.id == business_id

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_with_bad_id(self):
        with pytest.raises(BusinessUnavailable):
            business_id = "does-not-exist"
            self.client.get_business(business_id)

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_with_unicode_chars(self):
        business_id = u'weingalerie-und-café-nö-berlin'
        resp = self.client.get_business(business_id)
        assert resp.business.id == business_id

    @int_vcr.use_cassette(**cassette_params)
    def test_get_business_with_locale_params(self):
        business_id = u'yelp-san-francisco'
        params = {
            'cc': 'CA',
            'lang': 'fr'
        }
        resp = self.client.get_business(business_id, **params)
        assert resp.business.id == business_id
