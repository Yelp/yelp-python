# -*- coding: UTF-8 -*-
import oauth2


class Authentication():
    def __init__(self, credentials):
        self.consumer_key = credentials['CONSUMER_KEY']
        self.consumer_secret = credentials['CONSUMER_SECRET']
        self.token = credentials['TOKEN']
        self.token_secret = credentials['TOKEN_SECRET']

        self.consumer = oauth2.Consumer(self.consumer_key, self.consumer_secret)
        self.oauth_token = oauth2.Token(self.token, self.token_secret)
