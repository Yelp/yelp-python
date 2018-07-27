# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from six import text_type as str

from yelp.obj.response_object import ResponseObject


class Attribute(ResponseObject):

    _schema = {"name": str, "value": str}
