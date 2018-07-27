# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import pytest
import responses


@pytest.fixture(autouse=True)
def activate_response_mocking():
    with responses.mock:
        yield
