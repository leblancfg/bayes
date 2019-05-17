#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import time

AUTHOR = 'Francois Leblanc'
SITENAME = 'Study Group - Doing Bayesian Data Analysis'
SITEURL = ''
SITETITLE = 'Bayesian Study Group'
SITESUBTITLE = 'A 10-Week Study Group on Bayesian Data Analysis'
SITELOGO = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Bayes_icon.svg/500px-Bayes_icon.svg.png'
FAVICON = '/img/icons/favicon.ico'

ROBOTS = 'index, follow'

THEME = 'Flex'
PATH = 'content'
TIMEZONE = 'America/Montreal'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pandoc_reader']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution',
    'version': '4.0',
    'slug': 'by'
}

COPYRIGHT_YEAR = time.strftime('%Y')
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Define Links
STATIC_PATHS = ['img', 'pdf', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
