# -*- coding: UTF-8 -*-
from yelp.obj.business import Business


class BusinessResponse(object):

    def __init__(self, response):
        self.response = response
        self.business = Business(self.response)
