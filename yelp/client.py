# -*- coding: utf-8 -*-
import requests
import six

from yelp.config import API_ROOT_URL
from yelp.endpoint.business import Business
from yelp.errors import YelpError


class Client(object):

    _endpoints = [Business]

    def __init__(self, api_key):
        self._session = requests.Session()
        self._session.headers.update(self._get_auth_header(api_key))
        self._define_request_methods()

    # Creates an instance of each endpoint class and adds the instances'
    # public singleton methods to Client. We do this to promote
    # modularity.
    def _define_request_methods(self):
        endpoint_instances = [endpoint_cls(self) for endpoint_cls in self._endpoints]
        for endpoint in endpoint_instances:
            for exposed_method_name in endpoint.exposed_methods:
                exposed_method = getattr(endpoint, exposed_method_name)
                setattr(self, exposed_method_name, exposed_method)

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
