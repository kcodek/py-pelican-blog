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

# we must tell Pelican where to look for the static media files 
STATIC_PATHS = ['img', 'pdf']


# We have the option to define where Pelican should look for our blog's pages. 
# By default Pelican expects them to be in the content/pages folder. 
# It is not necessary to state the path but it is a good practice to do so. 
PAGE_PATHS = ['pages']

#To change the URL to show the content type and date as well. 
# The ARTICLE_URL variable states what should display in the web browser's address bar 
# while the ARTICLE_SAVE_AS variable defines where the article being generated should be output to.
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


#For pages, categories, and tags. 
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'