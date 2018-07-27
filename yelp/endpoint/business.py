# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from yelp.config import BUSINESS_PATH
from yelp.obj.business import Business


class BusinessEndpoints(object):
    def __init__(self, client):
        self.client = client

    def get_by_id(self, business_id, **url_params):
        """Make a request to the business details endpoint. More info at
        https://www.yelp.com/developers/documentation/v3/business

        Args:
            business_id (str): The business alias (i.e. yelp-san-francisco) or
                ID (i.e. 4kMBvIEWPxWkWKFN__8SxQ.
            **url_params: Dict corresponding to business API params
                https://www.yelp.com/developers/documentation/v3/business

        Returns:
            yelp.obj.business.Business object that wraps the response.

        """
        business_path = BUSINESS_PATH.format(business_id=business_id)
        response = self.client._make_request(business_path, url_params=url_params)
        return Business(response)
