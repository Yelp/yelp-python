# -*- coding: utf-8 -*-
from yelp.obj.response_object import ResponseObject


class Category(ResponseObject):

    _schema = {"alias": str, "title": str}
