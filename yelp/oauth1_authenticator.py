# -*- coding: UTF-8 -*-
import oauth2


class Oauth1Authenticator(object):

    def __init__(
        self,
        consumer_key,
        consumer_secret,
        token,
        token_secret
    ):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token, token_secret)

    def sign_request(self, url, url_params={}):
        oauth_request = oauth2.Request(
            method="GET",
            url=url,
            parameters=url_params
        )
        oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': self.token.key,
                'oauth_consumer_key': self.consumer.key
            }
        )
        oauth_request.sign_request(
            oauth2.SignatureMethod_HMAC_SHA1(),
            self.consumer,
            self.token
        )
        return oauth_request.to_url()
