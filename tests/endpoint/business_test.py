# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import mock
import pytest

import yelp.endpoint.business
from yelp.endpoint.business import BusinessEndpoints


@pytest.fixture
def business_endpoints(mock_client):
    return BusinessEndpoints(mock_client)


@pytest.fixture
def mock_business_response_cls():
    with mock.patch.object(
        yelp.endpoint.business, "Business"
    ) as mock_business_response_cls:
        yield mock_business_response_cls


class TestBusiness:
    def test_no_url_params(
        self, business_endpoints, mock_client, mock_business_response_cls
    ):
        business_endpoints.get_by_id("test-id")

        mock_client._make_request.assert_called_once_with(
            "/v3/businesses/test-id", url_params={}
        )
        assert mock_business_response_cls.called

    def test_with_url_params(
        self, business_endpoints, mock_client, mock_business_response_cls
    ):
        business_endpoints.get_by_id("test-id", locale="fr_FR")

        mock_client._make_request.assert_called_once_with(
            "/v3/businesses/test-id", url_params={"locale": "fr_FR"}
        )
        assert mock_business_response_cls.called
