# -*- coding: UTF-8 -*-
import mock
import pytest
import urllib2


from yelp.errors import ErrorHandler
from yelp.errors import InvalidParameter


class TestErrorHandler(object):

    @classmethod
    def setup_class(cls):
        cls.handler = ErrorHandler()

    def test_error_handler_throws_unknown_HTTPError(self):
        error = urllib2.HTTPError('', 400, 'Bad Request', None, None)
        error.read = mock.Mock()
        error.read.return_value = '{}'

        with pytest.raises(urllib2.HTTPError):
            self.handler.raise_error(error)

    def test_error_handler_raises_correct_yelp_error(self):
        with open('json/error_response.json') as resp_file:
            response = resp_file.read().replace('\n', '')

        error = mock.Mock()
        error.code = 400
        error.msg = 'Bad Request'
        error.read.return_value = response

        with pytest.raises(InvalidParameter) as err:
            self.handler.raise_error(error)
        assert "radius_filter" in err.value.text
