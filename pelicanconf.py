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

EMAIL_ADDRESS = 'aleksander@chrabasz.cz'
GITHUB_ADDRESS = 'https://github.com/alchrabas/blog'
TWITTER_ADDRESS = 'https://twitter.com/alchrabas'
LINKEDIN_ADDRESS = 'https://www.linkedin.com/in/aleksander-chrab%C4%85szcz-ab256513a/'

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


# Monkey patch to make PHP snippets highlight without <?php
from pygments.lexers.web import PhpLexer

if not hasattr(PhpLexer, '_wrapped_init'):
    PhpLexer._wrapped_init = PhpLexer.__init__
    def new_php_init(self, **options):
        options['_startinline'] = True
        PhpLexer._wrapped_init(self, **options)
    PhpLexer.__init__ = new_php_init

