# -*- coding: UTF-8 -*-
import json


class YelpError(Exception):

    def __init__(self, code, msg, response):
        self.code = code
        self.msg = msg

        self.id = response['error']['id']
        self.text = response['error']['text']


class InternalError(YelpError):
    pass


class ExceededReqs(YelpError):
    pass


class MissingParameter(YelpError):
    pass


class InvalidSignature(YelpError):
    pass


class InvalidOAuthCredentials(YelpError):
    pass


class InvalidOAuthUser(YelpError):
    pass


class AccountUnconfirmed(YelpError):
    pass


class UnavailableForLocation(YelpError):
    pass


class AreaTooLarge(YelpError):
    pass


class MultipleLocations(YelpError):
    pass


class BusinessUnavailable(YelpError):
    pass


class InvalidParameter(YelpError):

    def __init__(self, code, msg, response):
        super(InvalidParameter, self).__init__(code, msg, response)
        self.text += ': ' + response['error']['field']


class ErrorHandler(object):

    _error_map = {
        'INTERNAL_ERROR': InternalError,
        'EXCEEDED_REQS': ExceededReqs,
        'MISSING_PARAMETER': MissingParameter,
        'INVALID_PARAMETER': InvalidParameter,
        'INVALID_SIGNATURE': InvalidSignature,
        'INVALID_OAUTH_CREDENTIALS': InvalidOAuthCredentials,
        'INVALID_OAUTH_USER': InvalidOAuthUser,
        'ACCOUNT_UNCONFIRMED': AccountUnconfirmed,
        'UNAVAILABLE_FOR_LOCATION': UnavailableForLocation,
        'AREA_TOO_LARGE': AreaTooLarge,
        'MULTIPLE_LOCATIONS': MultipleLocations,
        'BUSINESS_UNAVAILABLE': BusinessUnavailable
    }

    def raise_error(self, error):
        response = json.loads(error.read())
        try:
            raise self._error_map[response['error']['id']](
                error.code,
                error.msg,
                response
            )
        except KeyError:
            raise error
