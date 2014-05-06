from __future__ import unicode_literals

AUTHOR = 'Chevah Team'
SITENAME = "Chevah Style Guide"

CONTACT = {
    'url': 'http://www.chevah.com',
    'email': 'contact@chevah.com',
    }

LINKS = {
    'github': 'http://github.com/chevah',
    'code': 'http://github.com/chevah/styleguide',
    }

#SITEURL = 'http://styleguide.chevah.com'

TIMEZONE = "Europe/London"
DEFAULT_DATE = 'fs'
DEFAULT_CATEGORY = 'misc'

FEED_DOMAIN = 'http://styleguide.chevah.com'
FEED_ATOM = None
FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

DEFAULT_METADATA = {'menu_order': '100'}

LOCALE = "C"

THEME = 'layout/'

# Where to save result.
OUTPUT_PATH = 'deploy/'
# Remove all files before creating new content.
DELETE_OUTPUT_DIRECTORY = True


FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'static',
    ]

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {}

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
