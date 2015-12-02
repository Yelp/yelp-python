# -*- coding: UTF-8 -*-
import mock

from yelp.client import Client
from yelp.obj.search_response import SearchResponse


class TestBusiness(object):

    @classmethod
    def setup_class(cls):
        auth = mock.Mock()
        cls.client = Client(auth)

    def test_phone_search_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = '{}'
            params = {
                'category': 'fashion'
            }
            response = self.client.phone_search('5555555555', **params)
            params['phone'] = '5555555555'
            request.assert_called_once_with('/v2/phone_search/', params)
            assert type(response) is SearchResponse
