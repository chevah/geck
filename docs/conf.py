# -*- coding: utf-8 -*-
#
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'C.G.E.C.K.'
copyright = u'2022, Chevah Team'
author = u'Chevah Team'

# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

language = None

exclude_patterns = []

pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_logo = '_static/chevah-logo.png'
html_theme_options = {
    'logo_only': True,
    'collapse_navigation': True,
    'display_version': False,
    'navigation_depth': 3,
}
