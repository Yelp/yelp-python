# -*- coding: utf-8 -*-
import pytest
from yelp.client import Client
import yelp.client
import mock


@pytest.fixture
def mock_requests():
    with mock.patch.object(yelp.client, "requests") as mock_requests:
        yield mock_requests


@pytest.fixture
def mock_client(mock_requests):
    return mock.Mock(name="Mock Client", spec=Client)
