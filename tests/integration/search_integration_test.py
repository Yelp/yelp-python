# -*- coding: UTF-8 -*-
import pytest

from tests.integration.integration_test import IntegrationTest
from yelp.errors import InvalidParameter
from yelp.obj.search_response import SearchResponse


class TestSearchIntegration(IntegrationTest):

    int_vcr = IntegrationTest.int_vcr
    cassette_params = IntegrationTest.cassette_params
    sample_location = 'San Francisco, CA'
    params_limit_one = {'limit': 1}

    @int_vcr.use_cassette(**cassette_params)
    def test_search_location_only(self):
        resp = self.client.search(self.sample_location)
        assert type(resp) is SearchResponse

    @int_vcr.use_cassette(**cassette_params)
    def test_search(self):
        resp = self.client.search(
            self.sample_location,
            **self.params_limit_one
        )
        assert len(resp.businesses) is 1

    @int_vcr.use_cassette(**cassette_params)
    def test_search_bad_params(self):
        with pytest.raises(InvalidParameter):
            params = {
                'limit': 'not_a_number'
            }
            self.client.search(self.sample_location, **params)

    @int_vcr.use_cassette(**cassette_params)
    def test_search_unicode_params(self):
        name = u'染太郎'
        unicode_params = {
            'term': name
        }
        resp = self.client.search(
            'Tokyo',
            **unicode_params
        )
        assert name in resp.businesses[0].id

    @int_vcr.use_cassette(**cassette_params)
    def test_search_by_bounding_box_only(self):
        resp = self.client.search_by_bounding_box(
            37.900000,
            -122.500000,
            37.788022,
            -122.399797,
            **self.params_limit_one)
        assert resp
        lat = resp.businesses[0].location.coordinate.latitude
        long = resp.businesses[0].location.coordinate.longitude
        assert (lat >= 37.788022 and lat <= 37.900000)
        assert (long >= -122.500000 and long <= -122.399797)

    @int_vcr.use_cassette(**cassette_params)
    def test_search_by_coordinates_only(self):
        resp = self.client.search_by_coordinates(37.788022, -122.399797)
        assert resp
