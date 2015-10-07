# -*- coding: UTF-8 -*-


class Review(object):

    def __init__(self, response):
        for key in response:
            setattr(self, key, response[key])
