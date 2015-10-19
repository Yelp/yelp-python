# -*- coding: UTF-8 -*-
from yelp.obj.deal import Deal
from yelp.obj.gift_certificate import GiftCertificate
from yelp.obj.location import Location
from yelp.obj.rating import Rating
from yelp.obj.review import Review


class Business(object):

    _fields = [
        'categories',
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
        'reservation_url',
        'review_count',
        'snippet_image_url',
        'snippet_text',
        'url'
    ]

    def __init__(self, response):
        for field in self._fields:
            value = response[field] if field in response else None
            self.__setattr__(field, value)

        self._parse_deals(response)
        self._parse_gift_certificates(response)
        self._parse_location(response)
        self._parse_rating(response)
        self._parse_reviews(response)

    # TODO: refactor below 3 functions into 1
    def _parse_deals(self, response):
        if 'deals' in response:
            self.deals = [Deal(d) for d in response['deals']]
        else:
            self.deals = None

    def _parse_gift_certificates(self, response):
        if 'gift_certificates' in response:
            self.gift_certificates = [
                GiftCertificate(gc) for gc in response['gift_certificates']
            ]
        else:
            self.gift_certificates = None

    def _parse_reviews(self, response):
        if 'reviews' in response:
            self.reviews = [Review(r) for r in response['reviews']]
        else:
            self.reviews = None

    def _parse_location(self, response):
        self.location = (
            Location(response['location']) if 'location' in response else None
        )

    def _parse_rating(self, response):
        self.rating = Rating(response) if 'rating' in response else None
