from setuptools import find_packages
from setuptools import setup

setup(
    name='yelp',

    version='1.0.1',

    description='Python Clientlib for Yelp Public API',

    url='https://github.com/Yelp/yelp-python',

    author='Yelp',
    author_email='partnerships@yelp.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'
    ],

    license='MIT',

    keywords='yelp',

    packages=find_packages(exclude=('tests*',)),

    install_requires=[
        'httplib2',
        'oauth2',
        'six',
    ],
)
