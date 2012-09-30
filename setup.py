# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='paulla.ircbot',
      version=version,
      description="a bot for ....",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='irc bot',
      author=u'Cyprien Le Pannérer',
      author_email='cyplp@free.fr',
      url='',
      license='gpl',
      packages=find_packages(),
# package_dir = {'':paulla},
      namespace_packages=['paulla'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'irckit',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      bot = paulla.ircbot:main
      """,
      )
