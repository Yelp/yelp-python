# -*- coding: UTF-8 -*-
import io

import mock
import pytest
import six

from tests.testing import resource_filename
from yelp.errors import ErrorHandler
from yelp.errors import InvalidParameter


class TestErrorHandler(object):

    @classmethod
    def setup_class(cls):
        cls.handler = ErrorHandler()

    def test_error_handler_throws_unknown_HTTPError(self):
        error = six.moves.urllib.error.HTTPError(
            '', 400, 'Bad Request', None, None)
        error.read = mock.Mock()
        error.read.return_value = b'{}'

        with pytest.raises(six.moves.urllib.error.HTTPError):
            self.handler.raise_error(error)

    def test_error_handler_raises_correct_yelp_error(self):
        with io.open(
                resource_filename('json/error_response.json'), 'rb',
        ) as resp_file:
            response = resp_file.read().replace(b'\n', b'')

        error = mock.Mock()
        error.code = 400
        error.msg = 'Bad Request'
        error.read.return_value = response

        with pytest.raises(InvalidParameter) as err:
            self.handler.raise_error(error)
        assert "radius_filter" in err.value.text
