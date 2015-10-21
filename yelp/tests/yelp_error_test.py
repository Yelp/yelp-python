# -*- coding: UTF-8 -*-
import mock
import pytest
import urllib2


from yelp.yelp_error import ErrorHandler
from yelp.yelp_error import InternalError
from yelp.yelp_error import InvalidOAuthUser
from yelp.yelp_error import InvalidParameter


class TestErrorHandler(object):

    @classmethod
    def setup_class(cls):
        cls.handler = ErrorHandler()

    def test_error_handler_class_names(self):
        assert self.handler._class_names['INTERNAL_ERROR'] == InternalError
        assert (
            self.handler._class_names['INVALID_OAUTH_USER'] == InvalidOAuthUser
        )

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
