#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Fabian Sarmiento'
SITENAME = u'Programarium'
SITEURL = 'http://localhost:8000'
SITETITLE = u'Programarium'
SITESUBTITLE = 'Algoritmos & Devs & Linux'
SITEDESCRIPTION = u'Web sobre algoritmos & Devs & Linux'
SITELOGO = '/static/logo.jpg'
PATH = 'content'
COPYRIGHT_YEAR = 2017

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', '#'),
          ('github', '#'),)

# Menu
MENUITEMS = (('Sobre Programarium', '#'),
                     ('Archivos', '#'),
                     ('Categorias', '#'),
                     ('Tags', '#'),)
DEFAULT_PAGINATION = 10

# Theme
THEME = '/home/server/pelican-themes/flex/'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Custom Home page
#DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
#PAGINATED_DIRECT_TEMPLATES = (('blog',))
#TEMPLATE_PAGES = {'home.html': 'index.html',}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
