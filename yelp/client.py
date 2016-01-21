# -*- coding: UTF-8 -*-
import inspect
import json

import six

from yelp.config import API_HOST
from yelp.endpoint.business import Business
from yelp.endpoint.phone_search import PhoneSearch
from yelp.endpoint.search import Search
from yelp.errors import ErrorHandler


class Client(object):

    _endpoints = [
        Business,
        PhoneSearch,
        Search
    ]

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self._error_handler = ErrorHandler()
        self._define_request_methods()

    # Creates an instance of each endpoint class and adds the instances' public
    # singleton methods to Client. We do this to promote modularity.
    def _define_request_methods(self):
        endpoint_instances = [end(self) for end in self._endpoints]
        for endpoint in endpoint_instances:
            instance_methods = inspect.getmembers(endpoint, inspect.ismethod)
            self._add_instance_methods(instance_methods)

    def _add_instance_methods(self, instance_methods):
        # instance_methods is a list of (name, value) tuples where value is the
        # instance of the bound method
        for method in instance_methods:
            if method[0][0] is not '_':
                self.__setattr__(method[0], method[1])

    def _make_request(self, path, url_params={}):
        url = 'https://{0}{1}?'.format(
            API_HOST,
            six.moves.urllib.parse.quote(path.encode('utf-8'))
        )
        signed_url = self.authenticator.sign_request(url, url_params)
        return self._make_connection(signed_url)

    def _make_connection(self, signed_url):
        try:
            conn = six.moves.urllib.request.urlopen(signed_url, None)
        except six.moves.urllib.error.HTTPError as error:
            self._error_handler.raise_error(error)
        else:
            try:
                response = json.loads(conn.read().decode('UTF-8'))
            finally:
                conn.close()
            return response
