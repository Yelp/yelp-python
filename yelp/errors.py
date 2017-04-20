# -*- coding: UTF-8 -*-
import json


class YelpError(Exception):

    def __init__(self, code, msg, response):
        self.code = code
        self.msg = msg

        self.id = response['error']['id']
        self.text = response['error']['text']

    def __str__(self):
        return repr({
            'code': self.code,
            'msg': self.msg,
            'id': self.id,
            'text': self.text,
        })


class AreaTooLarge(YelpError):
    pass


class BadCategory(YelpError):
    pass


class BusinessUnavailable(YelpError):
    pass


class ExceededReqs(YelpError):
    pass


class InternalError(YelpError):
    pass


class InvalidOAuthCredentials(YelpError):
    pass


class InvalidOAuthUser(YelpError):
    pass


class InvalidSignature(YelpError):
    pass


class MissingParameter(YelpError):
    pass


class MultipleLocations(YelpError):
    pass


class SSLRequired(YelpError):
    pass


class UnavailableForLocation(YelpError):
    pass


class UnspecifiedLocation(YelpError):
    pass


class InvalidParameter(YelpError):

    def __init__(self, code, msg, response):
        super(InvalidParameter, self).__init__(code, msg, response)
        self.text += ': ' + response['error']['field']


class ErrorHandler(object):

    _error_map = {
        'AREA_TOO_LARGE': AreaTooLarge,
        'BAD_CATEGORY': BadCategory,
        'BUSINESS_UNAVAILABLE': BusinessUnavailable,
        'EXCEEDED_REQS': ExceededReqs,
        'INTERNAL_ERROR': InternalError,
        'INVALID_OAUTH_CREDENTIALS': InvalidOAuthCredentials,
        'INVALID_OAUTH_USER': InvalidOAuthUser,
        'INVALID_SIGNATURE': InvalidSignature,
        'INVALID_PARAMETER': InvalidParameter,
        'MISSING_PARAMETER': MissingParameter,
        'MULTIPLE_LOCATIONS': MultipleLocations,
        'SSL_REQUIRED': SSLRequired,
        'UNAVAILABLE_FOR_LOCATION': UnavailableForLocation,
        'UNSPECIFIED_LOCATION': UnspecifiedLocation
    }

    def raise_error(self, error):
        response = json.loads(error.read().decode('UTF-8'))
        try:
            raise self._error_map[response['error']['id']](
                error.code,
                error.msg,
                response
            )
        except KeyError:
            raise error
