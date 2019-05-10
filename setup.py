#!/usr/bin/env python3
from setuptools import setup
from tplgen import __version__


setup(name='tplgen',
      version=__version__,
      description='Generic template generation tool',
      url='http://git.davepedu.com/dave/tplgen',
      author='dpedu',
      author_email='dave@davepedu.com',
      packages=['tplgen'],
      entry_points={
          "console_scripts": [
              "tplgen = tplgen:main"
          ]
      })
