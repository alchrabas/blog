#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aleksander Chrabąszcz'
SITENAME = 'alchrabas\' Blog'
SITEURL = '.' # https://alchrabas.pl

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'
DEFAULT_DATE_FORMAT = '%d %B %Y'
LOCALE = "en_US.utf8"

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'crowsfoot'
SITESUBTITLE = 'a private blog of Aleksander Chrabąszcz'
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images']
PROFILE_IMAGE_URL = "/images/transparent-logo-180.png"

EMAIL_ADDRESS = 'alchrabas@alchrabas.pl'
GITHUB_ADDRESS = 'https://github.com/alchrabas/blog-alchrabas'
TWITTER_ADDRESS = 'https://twitter.com/alchrabas'

"""
# Blogroll
LINKS = (('Taiga.io', 'https://tree.taiga.io/project/greekpl-exeris/'),
         ('Github repository', 'https://github.com/alchrabas/exeris'),
         ('Forum', 'https://forum.exeris.org/'),
        )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/exerisorg'),
         )
"""

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

INDEX_SAVE_AS = 'blog.html'
DISPLAY_INDEX_ON_MENU = True

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['share_post']


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

