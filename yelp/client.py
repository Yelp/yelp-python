# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import requests
import six

from yelp.config import API_ROOT_URL
from yelp.endpoint.business import BusinessEndpoints
from yelp.errors import YelpError


class Client(object):
    def __init__(self, api_key):
        self._session = requests.Session()
        self._session.headers.update(self._get_auth_header(api_key))

        # Add endpoints to this client. Then they will be accessed e.g.
        # client.business.get_by_id('yelp-san-francisco')
        self.business = BusinessEndpoints(self)

    def _make_request(self, path, url_params=None):
        url_params = url_params if url_params is not None else {}

        url = "{}{}".format(
            API_ROOT_URL, six.moves.urllib.parse.quote(path.encode("utf-8"))
        )

        response = self._session.get(url, params=url_params)

        if response.status_code == 200:
            return response.json()
        else:
            raise YelpError.from_response(response)

    def _get_auth_header(self, api_key):
        return {"Authorization": "Bearer {api_key}".format(api_key=api_key)}
