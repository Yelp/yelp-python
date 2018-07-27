# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from yelp.obj.response_object import ResponseObject


class DogFood(ResponseObject):
    _schema = {"brand": str, "cost": float}


class Place(ResponseObject):
    _schema = {"name": str}


class Dog(ResponseObject):
    _schema = {
        "name": str,
        "aliases": [str],
        "favorite_food": DogFood,
        "favorite_places": [Place],
    }


dog_obj = Dog(
    name="Master Peabody",
    aliases=["Woofus", "Dogmeat"],
    favorite_food=DogFood(brand="Kibbles", cost=9.99),
    favorite_places=[Place(name="dirt pile"), Place(name="fire hydrant")],
)


def test_repr():
    expected_py3 = (
        "Dog(aliases=['Woofus', 'Dogmeat'], "
        "favorite_food=DogFood(brand='Kibbles', cost=9.99), "
        "favorite_places=[Place(name='dirt pile'), Place(name='fire hydrant')], "
        "name='Master Peabody')"
    )
    expected_py27 = (
        "Dog(aliases=[u'Woofus', u'Dogmeat'], "
        "favorite_food=DogFood(brand=u'Kibbles', cost=9.99), "
        "favorite_places=[Place(name=u'dirt pile'), Place(name=u'fire hydrant')], "
        "name=u'Master Peabody')"
    )

    assert repr(dog_obj) in {expected_py27, expected_py3}
