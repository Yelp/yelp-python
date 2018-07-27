# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from six import text_type as str

from yelp.obj.response_object import ResponseObject


class Category(ResponseObject):

    _schema = {"alias": str, "title": str}
