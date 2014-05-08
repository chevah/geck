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

SITEURL = 'http://styleguide.chevah.com'

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

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

DEFAULT_METADATA = {'menu_order': '100'}

LOCALE = "C"

# Where to look for content pages.
PATH = 'content'

# Where to look for template and static files.
THEME = 'layout/'
# Where to copy static files on output.
THEME_STATIC_DIR = 'static/'
# What static folders to use from theme. Relative to THEME.
THEME_STATIC_PATHS = ['static']

# Where to save result.
OUTPUT_PATH = 'deploy/'
# Remove all files before creating new content.
DELETE_OUTPUT_DIRECTORY = True

# static paths will be copied without parsing their contents
# Relative to PATH
STATIC_PATHS = [
    '../CNAME',
    ]

EXTRA_PATH_METADATA = {
    '../CNAME': {'path': 'CNAME'},
    }

PYGMENTS_RST_OPTIONS = {}
