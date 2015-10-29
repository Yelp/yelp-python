# -*- coding: UTF-8 -*-


class ResponseObject(object):
    _fields = []

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

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
