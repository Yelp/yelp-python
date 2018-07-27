# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import pytest
import responses

import testing.business_lookup_responses as response_fixtures
import testing.obj.business as business_obj_fixtures
from testing.error_responses import ERROR_RESPONSES
from yelp import errors
from yelp.client import Client


class TestBusinessIntegration:
    @pytest.mark.parametrize(
        ["business_alias", "url_params", "mock_response", "expected_response"],
        [
            (
                "yelp-san-francisco",
                {},
                response_fixtures.YELP_SAN_FRANCISCO,
                business_obj_fixtures.yelp_san_francisco,
            ),
            (
                "basilique-du-sacré-cœur-de-montmartre-paris-3",
                {"locale": "fr_FR"},
                response_fixtures.SACRE_COEUR_PARIS,
                business_obj_fixtures.sacre_coeur_paris,
            ),
        ],
    )
    def test_success(
        self, business_alias, url_params, mock_response, expected_response
    ):
        responses.add(mock_response)
        client = Client("BOGUS API KEY")
        response = client.business.get_by_id(business_alias, **url_params)
        assert response.to_dict() == expected_response.to_dict()

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
            client.business.get_by_id("fake-business-alias", url_params=url_params)
