# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import responses


ERROR_RESPONSES = {
    "VALIDATION_ERROR": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias?locale=en_USS",
        json={
            "error": {
                "code": "VALIDATION_ERROR",
                "description": "'en_USS' does not match '^[a-z]{2,3}_[A-Z]{2}$'",
                "field": "locale",
                "instance": "en_USS",
            }
        },
        status=400,
    ),
    "INVALID_LOCALE": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias?locale=jp_US",
        json={
            "error": {
                "code": "INVALID_LOCALE",
                "description": "The locale you specified is not valid.",
            }
        },
        status=400,
    ),
    "INVALID_AUTHORIZATION_METHOD": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "INVALID_AUTHORIZATION_METHOD",
                "description": "Invalid authorization method supplied.",
            }
        },
        status=400,
    ),
    "UNAUTHORIZED_ACCESS_TOKEN": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "UNAUTHORIZED_ACCESS_TOKEN",
                "description": (
                    "The access token provided is not currently able to query "
                    "this endpoint."
                ),
            }
        },
        status=401,
    ),
    "TOKEN_INVALID": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "TOKEN_INVALID",
                "description": "Invalid access token or authorization header.",
            }
        },
        status=401,
    ),
    "BUSINESS_UNAVAILABLE": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "BUSINESS_UNAVAILABLE",
                "description": (
                    "We may not be able to provide details for certain "
                    "businesses, for example if they do not have any reviews yet."
                ),
            }
        },
        status=403,
    ),
    "BUSINESS_NOT_FOUND": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "BUSINESS_NOT_FOUND",
                "description": "The requested business could not be found.",
            }
        },
        status=404,
    ),
    "TOO_MANY_REQUESTS_PER_SECOND": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "TOO_MANY_REQUESTS_PER_SECOND",
                "description": (
                    "You have exceeded the queries-per-second limit for this "
                    "endpoint. Try reducing the rate at which you make queries."
                ),
            }
        },
        status=429,
    ),
    "ACCESS_LIMIT_REACHED": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "ACCESS_LIMIT_REACHED",
                "description": (
                    "You've reached the access limit for this client. See "
                    "instructions for requesting a higher access limit at "
                    "https://www.yelp.com/developers/documentation/v3/rate_limiting"
                ),
            }
        },
        status=429,
    ),
    "INTERNAL_ERROR": responses.Response(
        method="GET",
        url="https://api.yelp.com/v3/businesses/fake-business-alias",
        json={
            "error": {
                "code": "INTERNAL_ERROR",
                "description": (
                    "Something went wrong internally, please try again later."
                ),
            }
        },
        status=500,
    ),
}
