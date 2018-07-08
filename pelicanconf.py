#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tim Sainburg'
SITENAME = 'Tim Sainburg'
SITESUBTITLE = 'PhD Student @ UCSD studying Psychology, Neuroscience, Anthropogeny, Animal Communication, and Machine Learning'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['assets']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
#
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True
IGNORE_FILES = ['.ipynb_checkpoints']
#Theme
THEME = "pelican-themes/Flex"

LINKS = (('Gentner Lab', 'http://gentnerlab.ucsd.edu'),('GitHub', 'https://github.com/timsainb'))
#SITELOGO = '/mnt/cube/tsainbur/Projects/github_repos/timsainburg_dot_com/timsainburg.com/imgs/TSainburg.jpg'
SITELOGO = 'img/TSainburg.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
