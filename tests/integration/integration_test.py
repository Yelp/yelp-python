# -*- coding: UTF-8 -*-
import io
import json

import vcr

from tests.testing import resource_filename
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


class IntegrationTest(object):

    int_vcr = vcr.VCR(
        cassette_library_dir=resource_filename('integration/vcr_cassettes'),
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
        with io.open(
                resource_filename('json/credentials_secret.json'),
        ) as cred:
            test_creds = json.load(cred)
            auth = Oauth1Authenticator(**test_creds)
            cls.client = Client(auth)
