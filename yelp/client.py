# -*- coding: UTF-8 -*-
import urllib

from yelp.config import API_HOST
from yelp.config import SEARCH_PATH
from yelp.config import BUSINESS_PATH

import oauth2

class Client():
    def __init__(self, authentication):
        self.authentication = authentication

    def request(self, path, url_params={}):
        url = 'http://{0}{1}?'.format(API_HOST, urllib.quote(path))
        return self.authentication.request(url, url_params)

    def get_business(self, business_id):
        business_path = BUSINESS_PATH + business_id
        return self.request(business_path)
