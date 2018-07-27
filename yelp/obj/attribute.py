# -*- coding: utf-8 -*-
from yelp.obj.response_object import ResponseObject


class Attribute(ResponseObject):

    _schema = {"name": str, "value": str}
