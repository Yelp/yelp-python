# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from yelp.obj.response_object import ResponseObject


class Coordinates(ResponseObject):

    _schema = {"latitude": float, "longitude": float}
