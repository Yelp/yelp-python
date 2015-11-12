# -*- coding: UTF-8 -*-
import io
import json

import mock
import pytest
import six

from tests.testing import resource_filename
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.obj.business_response import BusinessResponse
from yelp.obj.search_response import SearchResponse


class TestClient(object):

    sample_location = 'San Francisco, CA'

    @classmethod
    def setup_class(cls):
        with io.open(resource_filename('json/credentials.json')) as cred:
            test_creds = json.load(cred)
            auth = Oauth1Authenticator(**test_creds)
            cls.client = Client(auth)

        with io.open(resource_filename('json/search_response.json')) as resp:
            cls.search_response = json.load(resp)
        with io.open(resource_filename('json/business_response.json')) as resp:
            cls.business_response = json.load(resp)

    def test_get_business_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = self.business_response
            response = self.client.get_business('test-id')
            request.assert_called_once_with('/v2/business/test-id', {})
            assert type(response) is BusinessResponse

    def test_get_business_builds_correct_params_with_lang(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = self.business_response
            params = {'lang': 'fr'}
            self.client.get_business('test-id', **params)
            request.assert_called_once_with('/v2/business/test-id', params)

    def test_search_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = self.search_response
            params = {
                'term': 'food',
            }
            response = self.client.search(self.sample_location, **params)
            params.update({
                'location': self.sample_location
            })
            request.assert_called_once_with('/v2/search/', params)
            assert type(response) is SearchResponse

    def test_search_builds_correct_params_with_current_lat_long(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            params = {
                'term': 'food',
            }
            self.client.search(self.sample_location, 0, 0, **params)
            params.update({
                'location': self.sample_location,
                'cll': '0,0'
            })
            request.assert_called_once_with('/v2/search/', params)

    def test_search_by_bounding_box_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            params = {
                'term': 'food',
            }
            self.client.search_by_bounding_box(0, 0, 0, 0, **params)
            params['bounds'] = '0,0|0,0'
            request.assert_called_once_with('/v2/search/', params)

    def test_search_by_coordinates_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            self.client.search_by_coordinates(0, 0, 0, 0, 0)
            request.assert_called_once_with('/v2/search/', {'ll': '0,0,0,0,0'})

    def test_phone_search_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = self.search_response
            params = {
                'category': 'fashion'
            }
            response = self.client.phone_search('5555555555', **params)
            params['phone'] = '5555555555'
            request.assert_called_once_with('/v2/phone_search/', params)
            assert type(response) is SearchResponse

    def test_make_connection_closes(self):
        mock_conn = mock.Mock()
        mock_conn.read.return_value = b"{}"
        with mock.patch(
                'six.moves.urllib.request.urlopen', return_value=mock_conn,
        ):
            self.client._make_connection("")
            mock_conn.close.assert_called_once_with()

    def test_make_connection_closes_with_exception(self):
        mock_conn = mock.Mock()
        mock_conn.read.side_effect = Exception
        with mock.patch(
                'six.moves.urllib.request.urlopen', return_value=mock_conn,
        ):
            with pytest.raises(Exception):
                self.client._make_connection("")
            mock_conn.close.assert_called_once_with()

    def test_make_request_calls_raise_error_on_HTTPError(self):
        error = six.moves.urllib.error.HTTPError(
            '', 400, 'Bad Request', None, None)
        error.read = mock.Mock()
        error.read.return_value = b'{}'

        with mock.patch('six.moves.urllib.request.urlopen', side_effect=error):
            with mock.patch('yelp.errors.ErrorHandler.raise_error') as r:
                self.client._make_request("")
                r.assert_called_once_with(error)
