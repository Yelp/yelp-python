# -*- coding: UTF-8 -*-
import io
import json

from tests.testing import resource_filename
from yelp.oauth1_authenticator import Oauth1Authenticator


class TestOauth1Authenticator(object):

    @classmethod
    def setup_class(cls):
        with io.open(resource_filename('json/credentials.json')) as cred:
            test_creds = json.load(cred)
            cls.auth = Oauth1Authenticator(**test_creds)

    def test_create_new_authentication(self):
        assert self.auth.consumer.key == 'consumer_key'
        assert self.auth.consumer.secret == 'consumer_secret'
        assert self.auth.token.key == 'token'
        assert self.auth.token.secret == 'token_secret'

    def test_sign_request(self):
        path = "https://api.yelp.com/"
        url = self.auth.sign_request(path)
        assert "oauth_consumer_key=consumer_key" in url
        assert "oauth_token=token" in url
        assert "oauth_signature_method=HMAC-SHA1" in url
