# -*- coding: UTF-8 -*-
from yelp.obj.coordinate import Coordinate
from yelp.obj.span import Span
from yelp.obj.response_object import ResponseObject


class Region(ResponseObject):

    def __init__(self, response):
        super(Region, self).__init__(response)

        self._parse('center', Coordinate, response)
        self._parse('span', Span, response)
