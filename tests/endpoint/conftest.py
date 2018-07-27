# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import mock
import pytest

import yelp.client
from yelp.client import Client


@pytest.fixture
def mock_requests():
    with mock.patch.object(yelp.client, "requests") as mock_requests:
        yield mock_requests


@pytest.fixture
def mock_client(mock_requests):
    return mock.Mock(name="Mock Client", spec=Client)
