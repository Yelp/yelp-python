# -*- coding: UTF-8 -*-
from yelp.obj.business import Business
from yelp.obj.response_object import ResponseObject


class BusinessResponse(ResponseObject):

    def __init__(self, response):
        super(BusinessResponse, self).__init__(response)

        self._parse_main_response_body('business', Business, response)
