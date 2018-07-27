# -*- coding: utf-8 -*-
from yelp.obj.response_object import ResponseObject


class DayHours(ResponseObject):

    _schema = {"day": int, "start": str, "end": str, "is_overnight": bool}


class Hours(ResponseObject):

    _schema = {"open": [DayHours], "hours_type": str, "is_open_now": bool}
