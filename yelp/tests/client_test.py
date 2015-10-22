# -*- coding: UTF-8 -*-
import json
import mock
import pytest
import urllib2

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.resp.business_response import BusinessResponse


class TestClient(object):

    @classmethod
    def setup_class(cls):
        with open('json/credentials_secret.json') as cred:
            test_creds = json.load(cred)
            auth = Oauth1Authenticator(**test_creds)
            cls.client = Client(auth)

    def test_make_connection_closes(self):
        mock_conn = mock.Mock()
        mock_conn.read.return_value = "{}"
        with mock.patch('yelp.client.urllib2.urlopen', return_value=mock_conn):
            self.client._make_connection("")
            mock_conn.close.assert_called_once_with()

    def test_make_connection_closes_with_exception(self):
        mock_conn = mock.Mock()
        mock_conn.read.side_effect = Exception
        with mock.patch('yelp.client.urllib2.urlopen', return_value=mock_conn):
            with pytest.raises(Exception):
                self.client._make_connection("")
            mock_conn.close.assert_called_once_with()

    # integration tests

    def test_url_with_no_params_throws_HTTPError(self):
        with pytest.raises(urllib2.HTTPError):
            self.client._make_request(path="/v2/business/")

    def test_get_business_returns_correct_id(self):
        id = "flour-water-san-francisco"
        resp = self.client.get_business(id)
        # assert resp['id'] == id
        assert type(resp) is BusinessResponse
        assert resp.business.id == id
