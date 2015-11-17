# -*- coding: UTF-8 -*-
from yelp.obj.response_object import ResponseObject


class Rating(ResponseObject):

    _fields = [
        'rating'
    ]

    # TODO: add option for small/large photos
    def __init__(self, response):
        super(Rating, self).__init__(response)

        # Review response uses 'rating_image_url' while Business response uses
        # 'rating_img_url' so check for both.
        if 'rating_image_url' in response:
            self.img_url = response['rating_image_url']
        elif 'rating_img_url' in response:
            self.img_url = response['rating_img_url']
        else:
            self.img_url = None
