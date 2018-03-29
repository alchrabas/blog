#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aleksander Chrabąszcz'
SITENAME = 'Commentarii'
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
SITESUBTITLE = 'Aleksander Chrabąszcz\'s Blog'
DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = ['images']
PROFILE_IMAGE_URL = "/images/transparent-logo-180.png"

EMAIL_ADDRESS = 'alchrabas@exeris.org'
GITHUB_ADDRESS = 'https://github.com/alchrabas/blog'
TWITTER_ADDRESS = 'https://twitter.com/alchrabas'


PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
                ('Home', '/'),
                ('Posts', '/posts.html'),
                ('About me', '/about.html'),
                ('My projects', '/projects.html'),
            )

INDEX_SAVE_AS = 'posts.html'
DISPLAY_INDEX_ON_MENU = False

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['share_post']


# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

