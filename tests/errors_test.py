# -*- coding: utf-8 -*-
from yelp.errors import YelpError
import mock
import pytest


def test():
    json_response = {
        "error": {
            "code": "AN_UNKNOWN_CODE_WHAT_COULD_IT_BE",
            "description": "A mystery description.",
        }
    }

    fake_response_with_unknown_error_code = mock.Mock(name="fake response")
    fake_response_with_unknown_error_code.json.return_value = json_response

    with pytest.raises(NotImplementedError):
        YelpError.from_response(fake_response_with_unknown_error_code)
