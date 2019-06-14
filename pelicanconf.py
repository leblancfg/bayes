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

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Social widget
LINKS = (
            ('Slack Channel', 'https://csps-efpc-daan.slack.com/messages/CKDHZQSH5/details/'),
            ('Textbook Website', 'http://www.indiana.edu/~kruschke/DoingBayesianDataAnalysis/'),
            ('Digital Academy', 'https://www.csps-efpc.gc.ca/About_us/Business_lines/digitalacademy-eng.aspx'),
         )

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
