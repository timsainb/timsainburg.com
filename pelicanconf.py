#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tim Sainburg'
SITENAME = 'Tim Sainburg'
SITESUBTITLE = 'PhD Student @ UCSD studying Psychology, Neuroscience, Anthropogeny, Animal Communication, and Machine Learning'
SITEURL = ''
SITEURL_ABS = 'https://timsainburg.com'

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
THEME = "custom_themes/Flex-TS"

LINKS = (
	('Gentner Lab', 'http://gentnerlab.ucsd.edu'),
#	('tsainbur@ucsd.edu', 'mailto:tsainbur@ucsd.edu')
	)
#SITELOGO = '/mnt/cube/tsainbur/Projects/github_repos/timsainburg_dot_com/timsainburg.com/imgs/TSainburg.jpg'
SITELOGO = 'img/TSainburg.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
COPYRIGHT_NAME="Tim Sainburg"
# Social widget
SOCIAL = (('twitter', 'http://twitter.com/tim_sainburg'),
          ('github', 'http://github.com/timsainb'),
          ('envelope', 'mailto:tsainbur@ucsd.edu'),
          ('google-scholar', 'https://scholar.google.com/citations?user=Koqjwg8AAAAJ'),
          )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GITHUB_URL = "https://github.com/timsainb"