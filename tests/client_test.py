# -*- coding: UTF-8 -*-
import mock
import pytest
import six

from yelp.client import Client


class TestClient(object):

    @classmethod
    def setup_class(cls):
        auth = mock.Mock()
        cls.client = Client(auth)

    def test_make_connection_closes(self):
        mock_conn = mock.Mock()
        mock_conn.read.return_value = b'{}'
        with mock.patch(
                'six.moves.urllib.request.urlopen', return_value=mock_conn,
        ):
            self.client._make_connection("")
            mock_conn.close.assert_called_once_with()

    def test_make_connection_closes_with_exception(self):
        mock_conn = mock.Mock()
        mock_conn.read.side_effect = Exception
        with mock.patch(
                'six.moves.urllib.request.urlopen', return_value=mock_conn,
        ):
            with pytest.raises(Exception):
                self.client._make_connection("")
            mock_conn.close.assert_called_once_with()

    def test_make_request_calls_raise_error_on_HTTPError(self):
        error = six.moves.urllib.error.HTTPError(
            '', 400, 'Bad Request', None, None)
        error.read = mock.Mock()
        error.read.return_value = b'{}'

        with mock.patch('six.moves.urllib.request.urlopen', side_effect=error):
            with mock.patch('yelp.errors.ErrorHandler.raise_error') as r:
                self.client._make_request("")
                r.assert_called_once_with(error)
