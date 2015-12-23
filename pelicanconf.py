#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mami'
SITENAME = u'Mami Blog'
SITEURL = 'https://mamix1116.github.io/pelican'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('<i class="fa-li fa fa-web"></i> mamipress', 'https://mamipress.main.jp'),
    ('<i class="fa-li fa fa-facebook"></i> Facebook', 'https://www.facebook.com/100009559792869'),
    ('<i class="fa-li fa fa-twitter"></i> Twitter', 'https://twitter.com/samael500'),
    ('<i class="fa-li fa fa-github"></i> Github', 'https://github.com/samael500'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# url and path settings
RELATIVE_URLS = True
CACHE_CONTENT = False
STATIC_PATHS = ['img']

THEME = 'themes/w3-personal-blog'