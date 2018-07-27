# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from six import text_type as str

from yelp.obj.response_object import ResponseObject


class Location(ResponseObject):

    _schema = {
        "display_address": [str],
        "address1": str,
        "address2": str,
        "address3": str,
        "city": str,
        "state": str,
        "zip_code": str,
        "country": str,
        "cross_streets": str,
    }
