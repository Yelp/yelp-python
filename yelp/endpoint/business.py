# -*- coding: UTF-8 -*-
from yelp.config import BUSINESS_PATH
from yelp.obj.business_response import BusinessResponse


class Business(object):

    def __init__(self, client):
        self.client = client

    def get_business(self, business_id, **url_params):
        """Make a request to the business endpoint. More info at
        https://www.yelp.com/developers/documentation/v2/business

        Args:
            business_id (str): The business id.
            **url_params: Dict corresponding to business API params
                https://www.yelp.com/developers/documentation/v2/business#lParam

        Returns:
            BusinessResponse object that wraps the response.

        """
        business_path = BUSINESS_PATH + business_id
        return BusinessResponse(
            self.client._make_request(business_path, url_params)
        )
