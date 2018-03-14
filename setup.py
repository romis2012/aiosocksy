#!/usr/bin/env python
import codecs
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = None

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'aiosocksy', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

if sys.version_info < (3, 5, 3):
    raise RuntimeError("aiosocks requires Python 3.5.3+")

setup(
    name='aiosocksy',
    author='Roman Snegirev',
    author_email='snegiryev@gmail.com',
    version=version,
    license='Apache 2',
    url='https://github.com/romis2012/aiosocksy',

    description=('SOCKS proxy client for aiohttp 3.0+. '
                 'See https://github.com/romis2012/aiosocksy '
                 'for more information'),
    packages=['aiosocksy'],
    keywords='socks proxy aiohttp',
    install_requires=[
        'aiohttp>=3.0',
    ],
)
