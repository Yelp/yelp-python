# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from yelp.obj.business import Business
from yelp.obj.category import Category
from yelp.obj.coordinates import Coordinates
from yelp.obj.hours import DayHours
from yelp.obj.hours import Hours
from yelp.obj.location import Location


yelp_san_francisco = Business(
    id="4kMBvIEWPxWkWKFN__8SxQ",
    alias="yelp-san-francisco",
    name="Yelp",
    image_url="https://s3-media2.fl.yelpcdn.com/bphoto/nQK-6_vZMt5n88zsAS94ew/o.jpg",
    is_claimed=True,
    is_closed=False,
    url="https://www.yelp.com/biz/yelp-san-francisco",
    phone="+14159083801",
    display_phone="(415) 908-3801",
    review_count=8422,
    categories=[Category(alias="massmedia", title="Mass Media")],
    rating=2.0,
    location=Location(
        display_address=["140 New Montgomery St", "San Francisco, CA 94105"],
        address1="140 New Montgomery St",
        address2="",
        address3="",
        city="San Francisco",
        state="CA",
        zip_code="94105",
        country="US",
        cross_streets="Natoma St & Minna St",
    ),
    coordinates=Coordinates(latitude=37.7867703362929, longitude=-122.399958372115),
    photos=[
        "https://s3-media2.fl.yelpcdn.com/bphoto/nQK-6_vZMt5n88zsAS94ew/o.jpg",
        "https://s3-media2.fl.yelpcdn.com/bphoto/yFHIb9gob4TzhKUemMOPww/o.jpg",
        "https://s3-media1.fl.yelpcdn.com/bphoto/EHCfkEpZraIfPl8gvCo1tg/o.jpg",
    ],
    hours=[
        Hours(
            open=[
                DayHours(day=0, start="0800", end="1800", is_overnight=False),
                DayHours(day=1, start="0800", end="1800", is_overnight=False),
                DayHours(day=2, start="0800", end="1800", is_overnight=False),
                DayHours(day=3, start="0800", end="1800", is_overnight=False),
                DayHours(day=4, start="0800", end="1800", is_overnight=False),
            ],
            hours_type="REGULAR",
            is_open_now=True,
        )
    ],
    transactions=[],
    attributes=None,
)


sacre_coeur_paris = Business(
    alias="basilique-du-sacré-cœur-de-montmartre-paris-3",
    attributes=None,
    categories=[
        Category(alias="churches", title="Église"),
        Category(alias="landmarks", title="Lieu & Bâtiment historique"),
    ],
    coordinates=Coordinates(latitude=48.886720769013, longitude=2.3430021056794),
    display_phone="01 53 41 89 00",
    hours=[
        Hours(
            hours_type="REGULAR",
            is_open_now=False,
            open=[
                DayHours(day=0, end="2230", is_overnight=False, start="0600"),
                DayHours(day=1, end="2230", is_overnight=False, start="0600"),
                DayHours(day=2, end="2230", is_overnight=False, start="0600"),
                DayHours(day=3, end="2230", is_overnight=False, start="0600"),
                DayHours(day=4, end="2230", is_overnight=False, start="0600"),
                DayHours(day=5, end="2230", is_overnight=False, start="0600"),
                DayHours(day=6, end="2230", is_overnight=False, start="0600"),
            ],
        )
    ],
    id="spIGAtquYQ0S7xai5eJSuA",
    image_url="https://s3-media2.fl.yelpcdn.com/bphoto/_jdFMkxKj8ejkD2dOduC1A/o.jpg",
    is_claimed=False,
    is_closed=False,
    location=Location(
        address1="35 rue du Chevalier de la Barre",
        address2="",
        address3="",
        city="Paris",
        country="FR",
        cross_streets="",
        display_address=["35 rue du Chevalier de la Barre", "75018 Paris"],
        state="75",
        zip_code="75018",
    ),
    name="Basilique du Sacré-Cœur de Montmartre",
    phone="+33153418900",
    photos=[
        "https://s3-media2.fl.yelpcdn.com/bphoto/_jdFMkxKj8ejkD2dOduC1A/o.jpg",
        "https://s3-media4.fl.yelpcdn.com/bphoto/xFFrnrUAPZYFvtZMLLWkvQ/o.jpg",
        "https://s3-media4.fl.yelpcdn.com/bphoto/70tWE7016eFJ-xjTup-YRA/o.jpg",
    ],
    rating=4.5,
    review_count=538,
    transactions=[],
    url="https://www.yelp.fr/biz/basilique-du-sacr%C3%A9-c%C5%93ur-de-montmartre-paris-3",  # noqa: E501
)
