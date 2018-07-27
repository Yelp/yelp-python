# -*- coding: utf-8 -*-
from yelp.obj.business import Business
from yelp.obj.location import Location
from yelp.obj.coordinates import Coordinates
from yelp.obj.category import Category
from yelp.obj.hours import Hours
from yelp.obj.hours import DayHours


biz_response_obj = Business(
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
