# -*- coding: UTF-8 -*-
import json
import vcr

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


class IntegrationTest(object):

    int_vcr = vcr.VCR(
        cassette_library_dir='integration/vcr_cassettes',
        match_on=['method'],
        path_transformer=vcr.VCR.ensure_suffix('.yaml')
    )
    cassette_params = {
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
