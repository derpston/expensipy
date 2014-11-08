#!/usr/bin/env python

from distutils.core import setup

setup(
      name = 'expensipy'
   ,  version = '0.0.1'
   ,  description = 'Fetches reports and expenses from Expensify'
   ,  long_description = """Expensify's API is not pleasant to use, so this \
project attempts to at least hide some of the horror from the user."""
   ,  author = 'Derp Ston'
   ,  author_email = 'derpston+pypi@sleepygeek.org'
   ,  url = 'https://github.com/derpston/expensipy'
   ,  py_modules=['expensipy']
   ,  requires = ['requests', 'yaml']
   )
