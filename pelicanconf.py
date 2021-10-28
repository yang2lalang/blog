#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Franklin OKOLI'
SITENAME = u'Franklin is Blogging'
SITEURL = 'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = 'Robotics Software Engineer, Part time Trader,  Consultant'
SITEDESCRIPTION = '%s\'s My thoughts and a few tutorials' % AUTHOR
SITELOGO = './images/cartoon_ik.png'

PATH = 'content'
RELATIVE_URLS = True
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

TIMEZONE = 'Europe/Paris'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (('Home', 'http://yang2lalang.com'),('Researchgate', 'https://www.researchgate.net/profile/Franklin_Okoli'),)


SOCIAL = (('linkedin', 'http://www.linkedin.com/in/franklinokoli/'),
	  ('github', 'https://github.com/yang2lalang'),
      ("rss", "/feeds/all.atom.xml"),
      )

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}


COPYRIGHT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 10

OUTPUT_PATH = 'docs/'
# Uncomment following line if you want document-relative URLs when developing
#

MARKUP = ('md')
STATIC_PATHS = ['images', 'extra','articles',"extra/CNAME","extra/custom.css"]
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap', 'post_stats','i18n_subsites']
IGNORE_FILES = ['.ipynb_checkpoints']
THEME = './Flex'

EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

CUSTOM_CSS = "extra/custom.css"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

DISQUS_SITENAME = "http-yang2lalang-github-io"
ADD_THIS_ID = 'ra-5bac97e477d3d598'

GOOGLE_ANALYTICS = "UA-126577907-1"


GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-9421131783612830',
    'page_level_ads': True,
    'ads': {
        'aside': '5340595560',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '9584371569',
        'article_top': '',
        'article_bottom': '7257980762',
    }
}
