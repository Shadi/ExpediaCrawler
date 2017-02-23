#!/usr/bin/env python

from distutils.core import setup

setup(name='ExpediaCrawler',
      version='1.0',
      description='Script to get flight offers from expedia on different days',
      url='https://github.com/Shadi-A/ExpediaCrawler',
      packages=['expediacrawler'],
      scripts=['crawl'],
      requires=['selenium', 'bs4', 'pyvirtualdisplay', 'lxml']
      )
