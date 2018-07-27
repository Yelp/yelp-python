# -*- coding: utf-8 -*-
import mock

from yelp.endpoint.business import Business as BusinessEndpoint
import yelp.endpoint.business
import pytest


@pytest.fixture
def business_endpoint(mock_client):
    return BusinessEndpoint(mock_client)


@pytest.fixture
def mock_business_response_cls():
    with mock.patch.object(
        yelp.endpoint.business, "BusinessResponse"
    ) as mock_business_response_cls:
        yield mock_business_response_cls


class TestBusiness:
    def test_no_url_params(
        self, business_endpoint, mock_client, mock_business_response_cls
    ):
        business_endpoint.get_business("test-id")

        mock_client._make_request.assert_called_once_with(
            "/v3/businesses/test-id", url_params={}
        )
        assert mock_business_response_cls.called

    def test_with_url_params(
        self, business_endpoint, mock_client, mock_business_response_cls
    ):
        business_endpoint.get_business("test-id", locale="fr_FR")

        mock_client._make_request.assert_called_once_with(
            "/v3/businesses/test-id", url_params={"locale": "fr_FR"}
        )
        assert mock_business_response_cls.called
