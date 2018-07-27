# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import json
import os.path


def read_json_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), "json", filename)
    with open(filepath) as f:
        return json.load(f)
