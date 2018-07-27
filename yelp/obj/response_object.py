# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


def dictify(obj):
    if isinstance(obj, ResponseObject):
        return {
            field_name: dictify(getattr(obj, field_name))
            for field_name in obj._schema.keys()
        }
    elif isinstance(obj, list):
        return [dictify(element) for element in obj]
    else:
        return obj


class ResponseObject(object):
    _schema = {}

    def __init__(self, response=None, **fields_to_values_override):
        self._field_names = sorted(self._schema)
        fields_to_values = {}

        if response is not None:
            for field_name, field_type in self._schema.items():
                raw_value = response.get(field_name)

                if raw_value is None:
                    value = None
                elif isinstance(field_type, list):
                    # If the schema is defined as a list, then the response
                    # data for this field is expected to be a list. For
                    # example, if the field_type is [str] then the data is
                    # expected to be a list of strings.
                    assert isinstance(raw_value, list)
                    element_type = field_type[0]
                    value = [element_type(element) for element in raw_value]
                else:
                    value = field_type(raw_value)

                fields_to_values[field_name] = value

        fields_to_values.update(fields_to_values_override)

        for field_name in self._field_names:
            field_value = fields_to_values[field_name]
            self.__setattr__(field_name, field_value)

    def __repr__(self):
        field_strings = []

        for field_name in self._field_names:
            field_value = getattr(self, field_name)
            field_str = "{}={}".format(field_name, repr(field_value))
            field_strings.append(field_str)

        return "{classname}({field_strings})".format(
            classname=type(self).__name__, field_strings=", ".join(field_strings)
        )

    __str__ = __repr__

    def to_dict(self):
        return dictify(self)
