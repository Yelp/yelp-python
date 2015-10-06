# -*- coding: UTF-8 -*-
import json
import urllib
import urllib2

from yelp.config import API_HOST
from yelp.config import BUSINESS_PATH


class Client():

    def __init__(self, authentication):
        self.authentication = authentication

    def request(self, path, url_params={}):
        url = 'http://{0}{1}?'.format(API_HOST, urllib.quote(path))
        signed_url = self.authentication.sign_request(url, url_params)

        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()

        return response

    def get_business(self, business_id):
        business_path = BUSINESS_PATH + business_id
        return self.request(business_path)
