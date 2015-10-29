# -*- coding: UTF-8 -*-
import json
import pytest
import vcr

from yelp.client import Client
from yelp.errors import BusinessUnavailable
from yelp.errors import InvalidParameter
from yelp.errors import MissingParameter
from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.obj.business_response import BusinessResponse
from yelp.obj.search_response import SearchResponse


class TestIntegration(object):

    sample_location = 'San Francisco, CA'
    params_limit_one = {'limit': 1}
    cassette_params = {
        'record_mode': 'new_episodes',
        'filter_query_parameters': [
            'oauth_consumer_key',
            'oauth_token',
            'oauth_body_hash',
            'oauth_nonce',
            'oauth_signature'
        ]
    }

    @classmethod
    def setup_class(cls):
        with open('json/credentials_secret.json') as cred:
            test_creds = json.load(cred)
            auth = Oauth1Authenticator(**test_creds)
            cls.client = Client(auth)

    @vcr.use_cassette('vcr_cassettes/business.yaml', **cassette_params)
    def test_url_with_no_params(self):
        with pytest.raises(MissingParameter):
            self.client.get_business('')

    @vcr.use_cassette('vcr_cassettes/business.yaml', **cassette_params)
    def test_get_business_returns_correct_result(self):
        id = "yelp-san-francisco"
        resp = self.client.get_business(id)
        assert type(resp) is BusinessResponse
        assert resp.business.id == id

    @vcr.use_cassette('vcr_cassettes/business.yaml', **cassette_params)
    def test_get_business_with_bad_id(self):
        with pytest.raises(BusinessUnavailable):
            id = "does-not-exist"
            self.client.get_business(id)

    @vcr.use_cassette('vcr_cassettes/business.yaml', **cassette_params)
    def test_get_business_with_unicode_chars(self):
        id = u'weingalerie-und-café-nö-berlin'
        resp = self.client.get_business(id)
        assert resp.business.id == id

    @vcr.use_cassette('vcr_cassettes/search.yaml', **cassette_params)
    def test_search_location_only(self):
        resp = self.client.search(self.sample_location)
        assert type(resp) is SearchResponse

    @vcr.use_cassette('vcr_cassettes/search.yaml', **cassette_params)
    def test_search(self):
        resp = self.client.search(
            self.sample_location,
            **self.params_limit_one
        )
        assert len(resp.businesses) is 1

    @vcr.use_cassette('vcr_cassettes/search.yaml', **cassette_params)
    def test_search_bad_params(self):
        with pytest.raises(InvalidParameter):
            params = {
                'limit': 'not_a_number'
            }
            self.client.search(self.sample_location, **params)

    @vcr.use_cassette('vcr_cassettes/search.yaml', **cassette_params)
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

    @vcr.use_cassette('vcr_cassettes/search.yaml', **cassette_params)
    def test_search_by_coordinates_only(self):
        resp = self.client.search_by_coordinates(37.788022, -122.399797)
        assert resp

    @vcr.use_cassette('vcr_cassettes/phone_search.yaml', **cassette_params)
    def test_phone_search(self):
        phone = '+14158267000'
        resp = self.client.phone_search(phone)
        assert type(resp) is SearchResponse
        assert phone in resp.businesses[0].phone
