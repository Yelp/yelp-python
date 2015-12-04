# -*- coding: UTF-8 -*-
from collections import namedtuple

from yelp.obj.deal import Deal
from yelp.obj.gift_certificate import GiftCertificate
from yelp.obj.location import Location
from yelp.obj.response_object import ResponseObject
from yelp.obj.review import Review


Category = namedtuple('Category', 'name alias')


class Business(ResponseObject):

    _fields = [
        'display_phone',
        'distance',
        'eat24_url',
        'id',
        'image_url',
        'is_claimed',
        'is_closed',
        'menu_provider',
        'menu_date_updated',
        'mobile_url',
        'name',
        'phone',
        'rating',
        'rating_img_url',
        'rating_img_url_small',
        'rating_img_url_large',
        'reservation_url',
        'review_count',
        'snippet_image_url',
        'snippet_text',
        'url'
    ]

    def __init__(self, response):
        super(Business, self).__init__(response)

        self._parse('deals', Deal, response)
        self._parse('gift_certificates', GiftCertificate, response)
        self._parse('reviews', Review, response)
        self._parse('location', Location, response)
        self._parse_categories(response)

    def _parse_categories(self, response):
        if 'categories' in response:
            self.categories = [
                Category(name, alias)
                for name, alias in response['categories']
            ]
        else:
            self.categories = None
