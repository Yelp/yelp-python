# -*- coding: UTF-8 -*-
import json
import sys


class ErrorHandler(object):

    _error_ids = [
        'INTERNAL_ERROR',
        'EXCEEDED_REQS',
        'MISSING_PARAMETER',
        'INVALID_PARAMETER',
        'INVALID_SIGNATURE',
        'INVALID_OAUTH_CREDENTIALS',
        'INVALID_OAUTH_USER',
        'ACCOUNT_UNCONFIRMED',
        'UNAVAILABLE_FOR_LOCATION',
        'AREA_TOO_LARGE',
        'MULTIPLE_LOCATIONS',
        'BUSINESS_UNAVAILABLE'
    ]

    def __init__(self):
        current_mod = sys.modules[__name__]
        self._class_names = {
            error_id: getattr(
                current_mod,
                self._convert_error_id_to_class_name(error_id)
            ) for error_id in self._error_ids
        }

    def raise_error(self, err):
        response = json.loads(err.read())
        try:
            raise self._class_names[response['error']['id']](
                err.code,
                err.msg,
                response
            )
        except KeyError:
            raise err

    def _convert_error_id_to_class_name(self, str):
        words = str.lower().split('_')
        return "".join(w.title() for w in words).replace('Oauth', 'OAuth')


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
