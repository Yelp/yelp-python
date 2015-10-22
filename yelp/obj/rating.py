# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class Rating(ResponseObject):

    _fields = [
        'rating'
    ]

    def __init__(self, response):
        super(Rating, self).__init__(response)

        # TODO: add option for small/large photos
        self.img_url = (
            response['rating_image_url']
            if 'rating_image_url' in response else None)
