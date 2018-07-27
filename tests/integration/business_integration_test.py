# -*- coding: utf-8 -*-
import pytest

from yelp import errors
from yelp.client import Client
import responses
from testing.error_responses import ERROR_RESPONSES
from testing.business_lookup_responses import BUSINESS_LOOKUP_RESPONSE
from testing.obj.business import biz_response_obj


class TestBusinessIntegration:
    def test_success(self):
        responses.add(BUSINESS_LOOKUP_RESPONSE)
        client = Client("BOGUS API KEY")
        response = client.get_business("yelp-san-francisco")
        assert response.to_dict() == biz_response_obj.to_dict()

    @pytest.mark.parametrize(
        ["url_params", "mock_response", "expected_error"],
        [
            (
                {"locale": "en_USS"},
                ERROR_RESPONSES["VALIDATION_ERROR"],
                errors.ValidationError,
            ),
            ({}, ERROR_RESPONSES["INVALID_LOCALE"], errors.InvalidLocale),
            (
                {},
                ERROR_RESPONSES["INVALID_AUTHORIZATION_METHOD"],
                errors.InvalidAuthorizationMethod,
            ),
            (
                {},
                ERROR_RESPONSES["UNAUTHORIZED_ACCESS_TOKEN"],
                errors.UnauthorizedAccessToken,
            ),
            ({}, ERROR_RESPONSES["TOKEN_INVALID"], errors.TokenInvalid),
            ({}, ERROR_RESPONSES["BUSINESS_UNAVAILABLE"], errors.BusinessUnavailable),
            ({}, ERROR_RESPONSES["BUSINESS_NOT_FOUND"], errors.BusinessNotFound),
            (
                {},
                ERROR_RESPONSES["TOO_MANY_REQUESTS_PER_SECOND"],
                errors.TooManyRequestsPerSecond,
            ),
            ({}, ERROR_RESPONSES["ACCESS_LIMIT_REACHED"], errors.AccessLimitReached),
            ({}, ERROR_RESPONSES["INTERNAL_ERROR"], errors.InternalError),
        ],
    )
    def test_errors(self, url_params, mock_response, expected_error):
        responses.add(mock_response)

        client = Client("BOGUS API KEY")
        with pytest.raises(expected_error):
            client.get_business("fake-business-alias", url_params=url_params)
