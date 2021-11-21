#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

TEMPLATE_EXTENSIONS = ['.gmi']
DIRECT_TEMPLATES = ['index']

AUTHOR = u'Anonymous'
SITENAME = u'Generic Capsule'
SITEURL = 'gemini://<MYURL>.net'
SITE_DESC = 'Just another gemlog'

PATH = 'content'
THEME = 'gemtext-pelican/'
OUTPUT_PATH = 'gemcap/'
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

FEED_ATOM = None
FEED_ALL_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_DOMAIN = SITEURL
RSS_FEED_SUMMARY_ONLY = False
WITH_FUTURE_DATE = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Thransoft', 'https://soft.thran.uk/'),
         ('You can modify those links in your config file', '#'),)


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# DATE CONFIG
DATE_FORMAT='%a %d %B %Y'
DEFAULT_DATE_FORMAT='%a %d %B %Y'

# PAGE OUTPUT URLS
PAGE_URL = '{slug}.gmi'
PAGE_SAVE_AS = '{slug}.gmi'
INDEX_SAVE_AS = 'index.gmi'

#AUTHOR_SAVE_AS = CATEGORY_SAVE_AS  = ARCHIVES_SAVE_AS = TAGS_SAVE_AS = None
#AUTHOR_URL = CATEGORY_URL  = ARCHIVES_URL = TAGS_URL = None

ARTICLE_URL = ARTICLE_SAVE_AS = 'gemlog/{category}/{date:%Y}/{date:%m}/{slug}.gmi'

