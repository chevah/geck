# -*- coding: utf-8 -*-
#
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = 'C.G.E.C.K.'
copyright = '2024, Chevah Team'
author = 'Chevah Team'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

language = 'en'

exclude_patterns = []

pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


html_theme = "furo"
html_static_path = ['_static']
html_theme_options = {
    'light_logo': 'chevah-logo.png',
    'dark_logo': 'chevah-logo.png',
}
