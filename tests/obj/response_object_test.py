# -*- coding: utf-8 -*-
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
    assert repr(dog_obj) == (
        "Dog(aliases=['Woofus', 'Dogmeat'], "
        "favorite_food=DogFood(brand='Kibbles', cost=9.99), "
        "favorite_places=[Place(name='dirt pile'), Place(name='fire hydrant')], "
        "name='Master Peabody')"
    )
