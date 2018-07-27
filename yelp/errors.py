# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class YelpError(Exception):
    required_fields = ["code", "description"]
    optional_fields = []

    def __init__(self, raw_response, **error_info):
        for field_name in self.required_fields:
            setattr(self, field_name, error_info[field_name])

        for field_name in self.optional_fields:
            setattr(self, field_name, error_info.get(field_name))

        self.raw_response = raw_response
        self.http_status = raw_response.status_code

    @staticmethod
    def from_response(raw_response):
        """The Yelp Fusion API returns error messages with a json body
        like:
        {
            'error': {
                'code': 'ALL_CAPS_CODE',
                'description': 'Human readable description.'
            }
        }

        Some errors may have additional fields. For example, a
        validation error:
        {
            'error': {
                'code': 'VALIDATION_ERROR',
                'description': "'en_USS' does not match '^[a-z]{2,3}_[A-Z]{2}$'",
                'field': 'locale',
                'instance': 'en_USS'
            }
        }
        """
        json_response = raw_response.json()
        error_info = json_response["error"]
        code = error_info["code"]

        try:
            error_cls = _error_map[code]
        except KeyError:
            raise NotImplementedError(
                "Unknown error code '{}' returned in Yelp API response. "
                "This code may have been newly added. Please ensure you are "
                "using the latest version of the yelp-python library, and if "
                "so, create a new issue at https://github.com/Yelp/yelp-python "
                "to add support for this error.".format(code)
            )
        else:
            return error_cls(raw_response, **error_info)


class ValidationError(YelpError):
    optional_fields = ["field", "instance"]


class InvalidLocale(YelpError):
    pass


class InvalidAuthorizationMethod(YelpError):
    pass


class UnauthorizedAccessToken(YelpError):
    pass


class TokenInvalid(YelpError):
    pass


class BusinessUnavailable(YelpError):
    pass


class BusinessNotFound(YelpError):
    pass


class TooManyRequestsPerSecond(YelpError):
    pass


class AccessLimitReached(YelpError):
    pass


class InternalError(YelpError):
    pass


_error_map = {
    "VALIDATION_ERROR": ValidationError,
    "INVALID_LOCALE": InvalidLocale,
    "INVALID_AUTHORIZATION_METHOD": InvalidAuthorizationMethod,
    "UNAUTHORIZED_ACCESS_TOKEN": UnauthorizedAccessToken,
    "TOKEN_INVALID": TokenInvalid,
    "BUSINESS_UNAVAILABLE": BusinessUnavailable,
    "BUSINESS_NOT_FOUND": BusinessNotFound,
    "TOO_MANY_REQUESTS_PER_SECOND": TooManyRequestsPerSecond,
    "ACCESS_LIMIT_REACHED": AccessLimitReached,
    "INTERNAL_ERROR": InternalError,
}
