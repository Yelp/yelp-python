from setuptools import setup

setup(
    name='yelp',

    version='1.0',

    description='Python Clientlib for Yelp Public API',

    url='https://github.com/Yelp/yelp-python',

    author='Yelp',
    author_email='partnerships@yelp.com',

    license='MIT',

    keywords='yelp',

    packages=[
        'yelp',
        'yelp.obj'
    ],

    install_requires=[
        'httplib2==0.9.2',
        'oauth2==1.9.0.post1'
    ],

    download_url='https://github.com/Yelp/yelp-python/tarball/1.0'
)
