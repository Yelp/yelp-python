# -*- coding: UTF-8 -*-
import json
import urllib
import urllib2

import oauth2

class Client():
    API_HOST = 'api.yelp.com'
    SEARCH_PATH = '/v2/search/'
    BUSINESS_PATH = '/v2/business/'

    def __init__(self, authentication):
        self.authentication = authentication

    def request(self, path, url_params={}):
        url = 'http://{0}{1}?'.format(self.API_HOST, urllib.quote(path))

        oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)
        oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': self.authentication.token,
                'oauth_consumer_key': self.authentication.consumer_key
            }
        )
        oauth_request.sign_request(
            oauth2.SignatureMethod_HMAC_SHA1(),
            self.authentication.consumer,
            self.authentication.oauth_token
        )
        signed_url = oauth_request.to_url()
        
        print u'Querying {0} ...'.format(url)

        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()

        return response

    def get_business(self, business_id):
        business_path = self.BUSINESS_PATH + business_id
        return self.request(business_path)
