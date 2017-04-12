#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Aaron Elmquist'
SITENAME = u'Leaked Memories'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Do not publish articles set in the future
WITH_FUTURE_DATES = True
TEMPLATE_PAGES = {'blog.html': 'blog.html'}
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Feed generation is usually not desired when developing
FEED_RSS = False
FEED_ATOM = False
FEED_ALL_RSS = False
FEED_ALL_ATOM = False
TRANSLATION_FEED_RSS = False
TRANSLATION_FEED_ATOM = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('Github', r'https://github.com/elmq0022'),
          ('LinkedIn', r'https://www.linkedin.com/in/aaron-elmquist-99800839/'),)

DEFAULT_PAGINATION = 10
DEFAULT_PAGINATION = True

PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
DIRECT_TEMPLATES = ('categories', 'index', 'blog-index', 'blog')

POST_LIMIT = 3

# PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Formatting for dates

DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

# Formatting for urls

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Plugins
###
# CONSIDER ADDING THESE
###

# PLUGIN_PATH = 'plugins'
# PLUGINS = ['sitemap', 'neighbors', 'related_posts']


# Specify theme

THEME = 'BT3-Flat'

SWIFTYPE = ''
SITE_THUMBNAIL = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
SITE_THUMBNAIL_TEXT = ' Leaked Memories'
SITESUBTITLE = 'Sharing my Experiences Coding'

# DISQUS_SITENAME = 'networktsukkomime'
# GOOGLE_ANALYTICS = ''
# GOOGLE_ANALYTICS_DOMAIN = 'networktsukkomi.me'

### Plugin-specific settings

RELATED_POSTS_MAX = 20

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


#===theme settings===========================

FAVICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
SHORTCUT_ICON = 'https://dl.dropboxusercontent.com/u/299446/logo.png'
HEADER_IMAGE = 'https://dl.dropboxusercontent.com/u/299446/logo-invert.png'
BACKGROUND_IMAGE = 'http://images.nationalgeographic.com/wpf/media-live/photos/000/763/cache/egret-fog-reflection_76312_990x742.jpg'
# COPYRIGHT = '2015 &copy; All Rights Reserved.'
# Google fonts can be downloaded with
# https://neverpanic.de/downloads/code/2014-03-19-downloading-google-web-fonts-for-local-hosting-fetch.sh'
# Maybe you need to add missing mime types to your webserver configuration
# USER_FONT = '/theme/fonts/font.css'
# USER_BOOTSTRAP = '//maxcdn.bootstrapcdn.com/bootstrap/3.3.4'
# USER_FONTAWESOME = '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0'
# USER_JQUERY = '//code.jquery.com/jquery-1.11.2.min.js'

# About ME
PERSONAL_PHOTO = ""
PERSONAL_INFO = """My Name is Aaron."""

# work
WORK_DESCRIPTION = ''
# items to descripe a work, "type", "cover-image link", "title", "descption", "link"
WORK_LIST = (('link', 
              'https://dl.dropboxusercontent.com/u/299446/BT3-Flat.png',
              'BT3-Flat',
              'A BT3 flat theme for pelican',
              'https://github.com/KenMercusLai/plumage'),
            )




#########################################################################################
SITEURL = ''


DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Theme Specific Settings

SITETITLE = 'Leaked Memories'
SITESUBTITLE = 'Sharing My Experiences in Coding'

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags/index.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors/index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'
ABOUT_ME_URL       = 'about-me'
ABOUT_ME_SAVE_AS   = 'about-me/index.html'


# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
    ('About Me', ABOUT_ME_URL, ABOUT_ME_SAVE_AS),
)

# additional menu 
# MENUITEMS = (
#     ('GitHub', 'https://github.com/'),
#     ('Linux Kernel', 'https://www.kernel.org/'),
# )

