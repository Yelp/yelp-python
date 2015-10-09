# -*- coding: UTF-8 -*-
import json
import urllib
import urllib2

from yelp.config import API_HOST
from yelp.config import BUSINESS_PATH
from yelp.config import SEARCH_PATH


class Client(object):

    def __init__(self, authenticator):
        self.authenticator = authenticator

    def get_business(self, business_id):
        business_path = BUSINESS_PATH + business_id
        return self._build_url(business_path)

    def search(
        self,
        location,
        **url_params
    ):
        url_params.update({
            'location': location.replace(' ', '+'),
        })
        if 'cll' in url_params:
            url_params['cll'] = self._format_cll(url_params['cll'])

        return self._build_url(SEARCH_PATH, url_params)

    def search_by_bounding_box(
        self,
        bounds,
        **url_params
    ):
        url_params['bounds'] = self._format_bounds(bounds)

        return self._build_url(SEARCH_PATH, url_params)

    def search_by_coordinates(
        self,
        coordinates,
        **url_params
    ):
        url_params['ll'] = self._format_coordinates(coordinates)

        return self._build_url(SEARCH_PATH, url_params)

    def _format_cll(self, cll):
        return '{0},{1}'.format(cll['latitude'], cll['longitude'])

    def _format_bounds(self, bounds):
        return '{0},{1}|{2},{3}'.format(
            bounds['sw_latitude'],
            bounds['sw_longitude'],
            bounds['ne_latitude'],
            bounds['ne_longitude']
        )

    def _format_coordinates(self, coordinates):
        coord = ''
        for key in coordinates:
            coord += str(coordinates[key]) + ','
        return coord[:-1]

    def _build_url(self, path, url_params={}):
        url = 'https://{0}{1}?'.format(API_HOST, urllib.quote(path))
        signed_url = self.authenticator.sign_request(url, url_params)
        return self._make_request(signed_url)

    def _make_request(self, signed_url):
        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()
        return response
