#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kcodek'
SITENAME = 'attetta'
SITEURL = ''

PATH = 'content'

OUTPUT_PATH = '../output'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
LINKS = (('Google ', 'https://google.com/'),
     ('Wikipedia', 'https://wikipedia.org'),)

SOCIAL = (('Twitter', 'https://twitter.com/mbdevaney'),
         ('Github', 'https://github.com/yourekittenme'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# tell Pelican where it can find the custom theme we will be using
THEME = 'theme'

# We must tell Pelican where the plugins folder is located
PLUGIN_PATHS = ['plugins/', ]

# Each plugin must be setup individually within pelicanconf.py. The PLUGINS variable contains all plugins being used by the website.
PLUGINS = ['i18n_subsites', ]

#The i18n_subsites plugin relies on a language called Jinja2. 
# To properly configure the i18n_subsites plugin we must also add the JINJA_ENVIRONMENT variable 
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


#Try pelican-bootstrap3 themes
BOOTSTRAP_THEME = 'flatly'


#Change the style of the code blocks
PYGMENTS_STYLE = 'monokai'
