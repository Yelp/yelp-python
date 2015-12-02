# -*- coding: UTF-8 -*-
import mock

from yelp.client import Client
from yelp.obj.search_response import SearchResponse


class TestBusiness(object):

    sample_location = 'San Francisco, CA'

    @classmethod
    def setup_class(cls):
        auth = mock.Mock()
        cls.client = Client(auth)

    def test_search_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            request.return_value = '{}'
            params = {
                'term': 'food',
            }
            response = self.client.search(self.sample_location, **params)
            params.update({
                'location': self.sample_location
            })
            request.assert_called_once_with('/v2/search/', params)
            assert type(response) is SearchResponse

    def test_search_builds_correct_params_with_current_lat_long(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            params = {
                'term': 'food',
            }
            self.client.search(self.sample_location, 0, 0, **params)
            params.update({
                'location': self.sample_location,
                'cll': '0,0'
            })
            request.assert_called_once_with('/v2/search/', params)

    def test_search_by_bounding_box_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            params = {
                'term': 'food',
            }
            self.client.search_by_bounding_box(0, 0, 0, 0, **params)
            params['bounds'] = '0,0|0,0'
            request.assert_called_once_with('/v2/search/', params)

    def test_search_by_coordinates_builds_correct_params(self):
        with mock.patch('yelp.client.Client._make_request') as request:
            self.client.search_by_coordinates(0, 0, 0, 0, 0)
            request.assert_called_once_with('/v2/search/', {'ll': '0,0,0,0,0'})
