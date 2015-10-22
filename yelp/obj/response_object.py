# -*- coding: UTF-8 -*-


class ResponseObject(object):
    _fields = []

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

    def _parse_list_to_objects(self, field_name, cls_name, response):
        self.__setattr__(
            field_name,
            (
                [cls_name(field) for field in response[field_name]]
                if field_name in response else None
            )
        )

    def _parse_one_to_object(self, field_name, cls_name, response):
        self.__setattr__(
            field_name,
            cls_name(response[field_name]) if field_name in response else None
        )
