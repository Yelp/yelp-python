# -*- coding: UTF-8 -*-
import json
import pytest
import urllib2

from yelp import authentication
from yelp import client as cli


class TestClient():

    def setup_method(self, method):
        with open('cred.json') as cred:
            test_creds = json.load(cred)
            auth = authentication.Authentication(test_creds)
            self.client = cli.Client(auth)

    def test_request_with_no_params_throws_HTTPError(self):
        with pytest.raises(urllib2.HTTPError):
            self.client.request(path="/v2/business/")

    def test_business(self):
        resp = self.client.get_business("flour-water-san-francisco")
        assert resp
