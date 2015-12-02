# -*- coding: UTF-8 -*-
import mock

from yelp.client import Client
from yelp.obj.business_response import BusinessResponse


class TestBusiness(object):

    @classmethod
    def setup_class(cls):
        auth = mock.Mock()
        cls.client = Client(auth)

    def test_get_business_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = '{}'
            response = self.client.get_business('test-id')
            request.assert_called_once_with('/v2/business/test-id', {})
            assert type(response) is BusinessResponse

    def test_get_business_builds_correct_params_with_lang(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            params = {'lang': 'fr'}
            self.client.get_business('test-id', **params)
            request.assert_called_once_with('/v2/business/test-id', params)
