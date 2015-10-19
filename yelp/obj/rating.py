# -*- coding: UTF-8 -*-


class Rating(object):

    def __init__(self, response):
        self.rating = response['rating'] if 'rating' in response else None

        # TODO: add option for small/large photos
        self.img_url = (
            response['rating_image_url']
            if 'rating_image_url' in response else None)
