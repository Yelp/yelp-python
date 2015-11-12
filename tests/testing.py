from __future__ import absolute_import
from __future__ import unicode_literals

import os.path


def resource_filename(filename):
    """Finds a filename rooted at tests/"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
