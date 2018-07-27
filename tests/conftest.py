# -*- coding: utf-8 -*-
import responses
import pytest


@pytest.fixture(autouse=True)
def activate_response_mocking():
    with responses.mock:
        yield
