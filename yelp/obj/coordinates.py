# -*- coding: utf-8 -*-
from yelp.obj.response_object import ResponseObject


class Coordinates(ResponseObject):

    _schema = {"latitude": float, "longitude": float}
