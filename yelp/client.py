# -*- coding: UTF-8 -*-
import json
import urllib
import urllib2

from yelp.config import API_HOST
from yelp.config import BUSINESS_PATH
from yelp.config import PHONE_SEARCH_PATH
from yelp.config import SEARCH_PATH
from yelp.errors import ErrorHandler
from yelp.resp.business_response import BusinessResponse
from yelp.obj.search_response import SearchResponse


class Client(object):

    def __init__(self, authenticator):
        self.authenticator = authenticator
        self._error_handler = ErrorHandler()

    def get_business(self, business_id):
        business_path = BUSINESS_PATH + business_id
        return BusinessResponse(self._make_request(business_path))

    def search(
        self,
        location,
        current_lat=None,
        current_long=None,
        **url_params
    ):
        url_params.update({
            'location': location
        })
        if current_lat is not None and current_long is not None:
            url_params['cll'] = self._format_current_lat_long(
                current_lat,
                current_long
            )

        return self._make_request(SEARCH_PATH, url_params)

    def search_by_bounding_box(
        self,
        sw_latitude,
        sw_longitude,
        ne_latitude,
        ne_longitude,
        **url_params
    ):
        url_params['bounds'] = self._format_bounds(
            sw_latitude,
            sw_longitude,
            ne_latitude,
            ne_longitude
        )

        return self._make_request(SEARCH_PATH, url_params)

    def search_by_coordinates(
        self,
        latitude,
        longitude,
        accuracy=None,
        altitude=None,
        altitude_accuracy=None,
        **url_params
    ):
        url_params['ll'] = self._format_coordinates(
            latitude,
            longitude,
            accuracy,
            altitude,
            altitude_accuracy
        )

        return self._make_request(SEARCH_PATH, url_params)

    def phone_search(self, phone, **url_params):
        url_params['phone'] = phone

        return SearchResponse(
            self._make_request(PHONE_SEARCH_PATH, url_params)
        )

    def _format_current_lat_long(self, lat, long):
        return '{0},{1}'.format(lat, long)

    def _format_bounds(
        self,
        sw_latitude,
        sw_longitude,
        ne_latitude,
        ne_longitude
    ):
        return '{0},{1}|{2},{3}'.format(
            sw_latitude,
            sw_longitude,
            ne_latitude,
            ne_longitude
        )

    def _format_coordinates(
        self,
        latitude,
        longitude,
        accuracy,
        altitude,
        altitude_accuracy
    ):
        coord = '{0},{1}'.format(latitude, longitude)
        for field in (accuracy, altitude, altitude_accuracy):
            if field is not None:
                coord += ',' + str(field)
            else:
                break
        return coord

    def _make_request(self, path, url_params={}):
        url = 'https://{0}{1}?'.format(API_HOST, urllib.quote(path))
        signed_url = self.authenticator.sign_request(url, url_params)
        return self._make_connection(signed_url)

    def _make_connection(self, signed_url):
        try:
            conn = urllib2.urlopen(signed_url, None)
        except urllib2.HTTPError as error:
            self._error_handler.raise_error(error)
        else:
            try:
                response = json.loads(conn.read())
            finally:
                conn.close()
            return response
