# -*- coding: UTF-8 -*-
import json
import urllib
import urllib2

from yelp.config import API_HOST
from yelp.config import BUSINESS_PATH
from yelp.resp.business_response import BusinessResponse


class Client(object):

    def __init__(self, authenticator):
        self.authenticator = authenticator

    def get_business(self, business_id):
        business_path = BUSINESS_PATH + business_id
        return BusinessResponse(self._build_url(business_path))

    def _build_url(self, path, url_params={}):
        url = 'https://{0}{1}?'.format(API_HOST, urllib.quote(path))
        signed_url = self.authenticator.sign_request(url, url_params)
        return self._make_request(signed_url)

    def _make_request(self, signed_url):
        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()
        return response
