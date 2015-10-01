# -*- coding: UTF-8 -*-
import json

from yelp import authentication


def test_create_new_authentication():
    with open('cred_sample.json') as cred:
        test_creds = json.load(cred)
        auth = authentication.Authentication(test_creds)
        assert auth.consumer_key == 'consumer_key'
        assert auth.consumer_secret == 'consumer_secret'
        assert auth.token == 'token'
        assert auth.token_secret == 'token_secret'
