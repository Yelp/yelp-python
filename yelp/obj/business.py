# -*- coding: UTF-8 -*-
from yelp.obj.deal import Deal
from yelp.obj.gift_certificate import GiftCertificate
from yelp.obj.location import Location
from yelp.obj.rating import Rating
from yelp.obj.response_object import ResponseObject
from yelp.obj.review import Review


class Business(ResponseObject):

    _fields = [
        'categories',
        'display_phone',
        'distance',
        'eat24_url',
        'id',  # access as business.business_id
        'image_url',
        'is_claimed',
        'is_closed',
        'menu_provider',
        'menu_date_updated',
        'mobile_url',
        'name',
        'phone',
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
        self._parse_main_response_body('rating', Rating, response)
