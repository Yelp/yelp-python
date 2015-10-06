# -*- coding: UTF-8 -*-
import json

from yelp.oauth1_authenticator import Oauth1Authenticator


def test_create_new_authentication():
    with open('cred_sample.json') as cred:
        test_creds = json.load(cred)
        auth = Oauth1Authenticator(**test_creds)

        assert auth.consumer.key == 'consumer_key'
        assert auth.consumer.secret == 'consumer_secret'
        assert auth.token.key == 'token'
        assert auth.token.secret == 'token_secret'
