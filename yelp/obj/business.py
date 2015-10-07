# -*- coding: UTF-8 -*-
from yelp.obj.review import Review


class Business(object):

    def __init__(self, response):
        for key in response:
            setattr(self, key, response[key])
        self._parse_reviews()

    def _parse_reviews(self):
        if hasattr(self, 'reviews'):
            review_list = []
            for r in self.reviews:
                review_list.append(Review(r))
            self.reviews = review_list
