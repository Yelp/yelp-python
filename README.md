[![Build Status](https://travis-ci.org/Yelp/yelp-python.svg?branch=master)](https://travis-ci.org/Yelp/yelp-python)
[![Coverage Status](https://img.shields.io/coveralls/Yelp/yelp-python.svg?branch=master)](https://coveralls.io/r/Yelp/yelp-python)

# yelp-python

A Python library for the [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3/get_started). It simplifies the process of request construction, and response parsing for Python developers. This clientlib is built and tested on Python 2.7 and 3.6.

Please file issues on this repository for bugs/feature requests for this python client. For bugs/features requests for the Yelp Fusion API itself, please open issues on the [dedicated Yelp Fusion repository](https://github.com/Yelp/yelp-fusion).


## Installation

Install yelp-python from PyPI using:

    pip install yelp

## Usage

### Basics

You must have a Yelp Fusion API key to make requests to the API. Sign up for an API key at https://www.yelp.com/developers/v3/manage_app. Instantiate `yelp.client.Client` with your API key, and start making requests!

```
from yelp.client import Client

MY_API_KEY = "abcefghijklmnopqrstuvqwxy123456789" #  Replace this with your real API key

client = Client(MY_API_KEY)
```

Now you can use the client object to make requests.

### Business Details Endpoint

Endpoint documentation: https://www.yelp.com/developers/documentation/v3/business

To query the Business Details Endpoint use the `busines.get_by_id` function with a Yelp business alias (i.e. `yelp-san-francisco`) or ID (i.e. `4kMBvIEWPxWkWKFN__8SxQ`). You can also pass in the locale parameter as specified in the [Business Details Endpoint Documentation](https://www.yelp.com/developers/documentation/v3/business).

```
> business_response = client.business.get_by_id('yelp-san-francisco')

> business_response
Business(alias='yelp-san-francisco', attributes=None, categories=[Category(alias='massmedia', title='Mass Media')], coordinates=Coordinates(latitude=37.7867703362929, longitude=-122.399958372115), display_phone='(415) 908-3801', hours=[Hours(hours_type='REGULAR', is_open_now=True, open=[DayHours(day=0, end='1800', is_overnight=False, start='0800'), DayHours(day=1, end='1800', is_overnight=False, start='0800'), DayHours(day=2, end='1800', is_overnight=False, start='0800'), DayHours(day=3, end='1800', is_overnight=False, start='0800'), DayHours(day=4, end='1800', is_overnight=False, start='0800')])], id='4kMBvIEWPxWkWKFN__8SxQ', image_url='https://s3-media2.fl.yelpcdn.com/bphoto/nQK-6_vZMt5n88zsAS94ew/o.jpg', is_claimed=True, is_closed=False, location=Location(address1='140 New Montgomery St', address2='', address3='', city='San Francisco', country='US', cross_streets='Natoma St & Minna St', display_address=['140 New Montgomery St', 'San Francisco, CA 94105'], state='CA', zip_code='94105'), name='Yelp', phone='+14159083801', photos=['https://s3-media2.fl.yelpcdn.com/bphoto/nQK-6_vZMt5n88zsAS94ew/o.jpg', 'https://s3-media2.fl.yelpcdn.com/bphoto/yFHIb9gob4TzhKUemMOPww/o.jpg', 'https://s3-media1.fl.yelpcdn.com/bphoto/EHCfkEpZraIfPl8gvCo1tg/o.jpg'], rating=2.0, review_count=8421, transactions=[], url='https://www.yelp.com/biz/yelp-san-francisco?adjust_creative=wpr6gw4FnptTrk1CeT8POg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_lookup&utm_source=wpr6gw4FnptTrk1CeT8POg')
```

## Contributing

1. Fork it (http://github.com/yelp/yelp-python/fork)
2. Setup your virtual environment
```
$ pip install tox
$ tox -e venv
$ . venv-yelp/bin/activate
```
3. Create your feature branch (git checkout -b my-new-feature)
4. Commit your changes (git commit -am 'Add some feature')
5. Push to the branch (git push origin my-new-feature)
6. Create new Pull Request

### Testing

Please write tests for any new features. We use pytest + tox so just run `tox` to run the full test suite.  Full py.test documentation [here](http://pytest.org/latest/contents.html).
