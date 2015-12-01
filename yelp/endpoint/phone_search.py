# -*- coding: UTF-8 -*-
from yelp.config import PHONE_SEARCH_PATH
from yelp.obj.search_response import SearchResponse


class PhoneSearch(object):

    def __init__(self, client):
        self.client = client

    def phone_search(self, phone, **url_params):
        """Make a request to the phone search endpoint.More info at
        https://www.yelp.com/developers/documentation/v2/phone_search

        Args:
            phone (str): Business phone number to search for.
            **url_params: Dict corresponding to phone search API params
                https://www.yelp.com/developers/documentation/v2/phone_search

        Returns:
            SearchResponse object that wraps the response.

        """
        url_params['phone'] = phone

        return SearchResponse(
            self.client._make_request(PHONE_SEARCH_PATH, url_params)
        )
