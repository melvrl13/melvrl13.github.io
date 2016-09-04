#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan L. Melvin'
SITENAME = 'odsap'
SITEURL = 'http://odsap.com'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/odsap'),
          ('linkedin', 'http://www.linkedin.com/in/ryan-melvin-834a8522'),
          ('github', 'http://github.com/melvrl13'),
          )

GITHUB_USER = 'melvrl13'
TWITTER_USERNAME = 'odsap'
TWITTER_CARDS = True


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

# Plugins and their necessities
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['ipynb.markup', 'sitemap', 'tipue_search', 'related_posts', 'tag_cloud', 'liquid_tags.notebook']
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
RELATED_POSTS_MAX = 10
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

THEME = '/home/melvrl13/PycharmProjects/odsap/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'cerulean'
PYGMENTS_STYLE = 'solarizeddark'
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

LOAD_CONTENT_CACHE = False
