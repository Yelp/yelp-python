# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from six import text_type as str

from yelp.obj.response_object import ResponseObject


class DayHours(ResponseObject):

    _schema = {"day": int, "start": str, "end": str, "is_overnight": bool}


class Hours(ResponseObject):

    _schema = {"open": [DayHours], "hours_type": str, "is_open_now": bool}
