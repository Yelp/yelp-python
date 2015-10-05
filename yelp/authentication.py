# -*- coding: UTF-8 -*-
import json
import oauth2
import urllib2


class Authentication():

    def __init__(self, credentials):
        self.consumer_key = credentials['CONSUMER_KEY']
        self.consumer_secret = credentials['CONSUMER_SECRET']
        self.token = credentials['TOKEN']
        self.token_secret = credentials['TOKEN_SECRET']

        self.consumer = oauth2.Consumer(
            self.consumer_key,
            self.consumer_secret
        )
        self.oauth_token = oauth2.Token(self.token, self.token_secret)

    def request(self, url, url_params={}):
        oauth_request = oauth2.Request(
            method="GET",
            url=url,
            parameters=url_params
        )
        oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': self.token,
                'oauth_consumer_key': self.consumer_key
            }
        )
        oauth_request.sign_request(
            oauth2.SignatureMethod_HMAC_SHA1(),
            self.consumer,
            self.oauth_token
        )
        signed_url = oauth_request.to_url()

        print u'Querying {0} ...'.format(url)

        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()

        return response
