# -*- coding: UTF-8 -*-
import json
import mock
import pytest
import urllib2

from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.client import Client


class TestClient(object):

    sample_location = "San Francisco, CA"
    params_limit_one = {
        'limit': 1
    }

    @classmethod
    def setup_class(cls):
        with open('json/credentials_secret.json') as cred:
            test_creds = json.load(cred)
            auth = Oauth1Authenticator(**test_creds)
            cls.client = Client(auth)

    def test_search_builds_correct_params(self):
        with mock.patch('yelp.client.Client._build_url') as build:
            params = {
                'term': 'food',
            }
            self.client.search(self.sample_location, **params)
            params.update({
                'location': self.sample_location.replace(' ', '+'),
            })
            build.assert_called_once_with('/v2/search/', params)

    def test_search_builds_correct_params_with_cll(self):
        with mock.patch('yelp.client.Client._build_url') as build:
            params = {
                'term': 'food',
                'cll': {
                    'latitude': 0,
                    'longitude': 0
                }
            }
            self.client.search(self.sample_location, **params)
            params.update({
                'location': self.sample_location.replace(' ', '+'),
                'cll': '0,0'
            })
            build.assert_called_once_with('/v2/search/', params)

    def test_search_by_bounding_box_builds_correct_params(self):
        with mock.patch('yelp.client.Client._build_url') as build:
            bounds = {
                'sw_latitude': 0,
                'sw_longitude': 0,
                'ne_latitude': 0,
                'ne_longitude': 0
            }
            params = {
                'term': 'food',
            }
            self.client.search_by_bounding_box(bounds, **params)
            params['bounds'] = '0,0|0,0'
            build.assert_called_once_with('/v2/search/', params)

    def test_search_by_coordinates_builds_correct_params(self):
        with mock.patch('yelp.client.Client._build_url') as build:
            coordinates = {
                'latitude': 0,
                'longitude': 0,
                'accuracy': 0,
                'altitude': 0,
                'altitude_accuracy': 0
            }
            self.client.search_by_coordinates(coordinates)
            build.assert_called_once_with('/v2/search/', {'ll': '0,0,0,0,0'})

    def test_make_request_connection_closes(self):
        mock_conn = mock.Mock()
        mock_conn.read.return_value = "{}"
        with mock.patch('yelp.client.urllib2.urlopen', return_value=mock_conn):
            self.client._make_request("")
            mock_conn.close.assert_called_once_with()

    def test_make_request_connection_closes_with_exception(self):
        mock_conn = mock.Mock()
        mock_conn.read.side_effect = Exception
        with mock.patch('yelp.client.urllib2.urlopen', return_value=mock_conn):
            with pytest.raises(Exception):
                self.client._make_request("")
            mock_conn.close.assert_called_once_with()

    # integration tests

    def test_url_with_no_params_throws_HTTPError(self):
        with pytest.raises(urllib2.HTTPError):
            self.client._build_url(path="/v2/business/")

    def test_get_business_returns_correct_result(self):
        id = "flour-water-san-francisco"
        resp = self.client.get_business(id)
        assert resp['id'] == id

    def test_search_location_only(self):
        resp = self.client.search(self.sample_location)
        assert resp

    def test_search(self):
        resp = self.client.search(
            self.sample_location,
            **self.params_limit_one
        )
        assert len(resp['businesses']) == 1

    def test_search_bad_params_throws_HTTPError(self):
        with pytest.raises(urllib2.HTTPError):
            params = {
                'limit': 'not_a_number'
            }
            self.client.search(self.sample_location, **params)

    def test_search_by_bounding_box_only(self):
        resp = self.client.search_by_bounding_box({
            'sw_latitude': 37.900000,
            'sw_longitude': -122.500000,
            'ne_latitude': 37.788022,
            'ne_longitude': -122.399797
        }, **self.params_limit_one)
        assert resp
        lat = resp['businesses'][0]['location']['coordinate']['latitude']
        long = resp['businesses'][0]['location']['coordinate']['longitude']
        assert (lat >= 37.788022 and lat <= 37.900000)
        assert (long >= -122.500000 and long <= -122.399797)

    def test_search_by_coordinates_only(self):
        resp = self.client.search_by_coordinates({
            'latitude': 37.788022,
            'longitude': -122.399797
        })
        assert resp
