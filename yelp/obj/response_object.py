# -*- coding: UTF-8 -*-
import re


class ResponseObject(object):
    _fields = []

    def __init__(self, response):
        for field in self._fields:
            field_name = (
                self._camel_case_to_underscore(self.__class__.__name__) + '_id'
                if field is 'id' else field
            )
            value = response[field] if field in response else None
            self.__setattr__(field_name, value)

    def _camel_case_to_underscore(self, string):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def _parse(self, field_name, cls_name, response):
        if response and field_name in response:
            if type(response[field_name]) is list:
                self._parse_list_to_objects(field_name, cls_name, response)
            else:
                self._parse_one_to_object(field_name, cls_name, response)
        else:
            self.__setattr__(field_name, None)

    def _parse_list_to_objects(self, field_name, cls_name, response):
        self.__setattr__(
            field_name,
            [cls_name(field) for field in response[field_name]]
        )

    def _parse_one_to_object(self, field_name, cls_name, response):
        self.__setattr__(
            field_name,
            cls_name(response[field_name])
        )

    # expect field in main response body as opposed to response[field_name]
    def _parse_main_response_body(self, field_name, cls_name, response):
        self.__setattr__(field_name, cls_name(response))
