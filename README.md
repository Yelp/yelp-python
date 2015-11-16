[![Build Status](https://travis-ci.org/Yelp/yelp-python.svg?branch=master)](https://travis-ci.org/Yelp/yelp-python)
[![Coverage Status](https://img.shields.io/coveralls/Yelp/yelp-python.svg?branch=master)](https://coveralls.io/r/Yelp/yelp-python)

# yelp-python

A Python library for the Yelp API. It simplifies the process of authentication, request construction, and response parsing for Python developers using the Yelp API. This clientlib is built and tested on Python 2.7 and 3.4.

## Installation

Install yelp-python from PyPI using:

    pip install yelp

## Usage

### Basics

The library uses a client object to query against the API. Make a client by creating an instance of `Oauth1Authenticator` with your API key and passing that to the client constructor. You can sign up for an API key at [https://www.yelp.com/developers/manage_api_keys](https://www.yelp.com/developers/manage_api_keys).

```
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)
```

To keep your API access keys secure, we highly recommend putting them in a file which you add to `.gitignore`. For example, store your keys in a file called `config_secret.json`.

```
{
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "token": "YOUR_TOKEN",
    "token_secret": "YOUR_TOKEN_SECRET"
}
```

Then load it into your code to construct a client.

```
# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)
```

Now you can use the client object to make requests.

### Search API

There are three ways to query the Search API: `search`, `search_by_bounding_box`, and `search_by_coordinates`. For each of these methods, additional parameters are optional. The full list of parameters can be found on the [Search API Documentation](https://www.yelp.com/developers/documentation/v2/search_api).

```
params = {
    'term': 'food',
    'lang': 'fr'
}

client.search('San Francisco', **params)
```

`search_by_bounding_box` takes a southwest latitude/longitude and a northeast latitude/longitude as the location boundary ([details](https://www.yelp.com/developers/documentation/v2/search_api#searchGBB)).

```
client.search_by_bounding_box(
    37.900000,
    -122.500000,
    37.788022,
    -122.399797,
    **params
)
```

`search_by_coordinates` takes a geographic coordinate ([details](https://www.yelp.com/developers/documentation/v2/search_api#searchGC)).

    client.search_by_coordinates(37.788022, -122.399797, **params)

### Business API

To query the Business API use the `get_business` function with a business id. You can also pass in locale parameters as specified in the [Business API Documentation](https://www.yelp.com/developers/documentation/v2/business).

```
params = {
    'lang': 'fr'
}

client.get_business('yelp-san-francisco', **params)
```

### Phone Search API

To query the Phone Search API use the `phone_search` function with a phone number. Additional parameters can be found on [Phone Search API Documentation](https://www.yelp.com/developers/documentation/v2/phone_search).

```
params = {
    'category': 'fashion'
}

client.phone_search('+15555555555', **params)
```

## Responses

Responses from the API are parsed into Python objects.

Search and phone search responses are parsed into `SearchResponse` objects.

```
>>> response = client.search('San Francisco')

>>> response.businesses
[<Business 1>, <Business 2>, ...]

>>> response.businesses[0].name
u'The Flying Falafel'

>>> response.businesses[0].rating.rating
4.5
```

Business responses are parsed into `BusinessResponse` objects.

```
>>> response = client.get_business('yelp-san-francisco')

>>> response.business.name
u'Yelp'

>>> response.business.categories
[Category(name=u'Local Flavor', alias=u'localflavor'), Category(name=u'Mass Media', alias=u'massmedia')]
```

For a full list of available response fields, take a look at the [documentation](https://www.yelp.com/developers/documentation/v2/overview) or the classes defined in `yelp/obj`.

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

If you are adding a new integration test, you will need to connect to the Yelp API. You can set this up by creating a file `tests/json/credentials_secret.json` that contains your API keys in the following format:

```
{
    "consumer_key": "YOUR_CONSUMER_KEY",
    "consumer_secret": "YOUR_CONSUMER_SECRET",
    "token": "YOUR_TOKEN",
    "token_secret": "YOUR_TOKEN_SECRET"
}
```

We use VCR.py to record and serialize HTTP requests. Add your test to `tests/integration_test.py` and use the decorator

    @int_vcr.use_cassette(**cassette_params)

The first time you run the test, VCR.py will record the HTTP request to the folder `/tests/integration/vcr_cassettes` in a yaml file of the same name as the test, filtering out your oauth tokens prior to writing. VCR.py will replay the response for subsequent runs. This allows us to have deterministic tests and continuously integrate with Travis CI. To clear the recorded response, delete the cassette file. Running the test again will make a new HTTP request and record it. For more information, see [VCR.py documentation](https://github.com/kevin1024/vcrpy).

### Git Workflow

We are using the [git flow](http://nvie.com/posts/a-successful-git-branching-model/)
workflow. Atlassian has a [solid overview](https://www.atlassian.com/git/workflows#!workflow-gitflow).
Essentially, new development is merged into the develop branch from feature
branches, then merged from develop to a release branch, then to master from
the release branch. Master should always contain the most recently released
version of the library.
