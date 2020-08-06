project = 'OneFootball Network API'
copyright = '2020, OneFootball'
author = 'OneFootball'

# Custom extension requires this.
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

master_doc = 'index'

# The full version, including alpha/beta/rc tags
release = '0.2'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'codeexample',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


html_theme = 'flask'
html_favicon = '_static/favicon.svg'
html_sidebars = { '**': ['localtoc.html'], }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

source_suffix = '.rst'

pygments_style = 'trac'

# LOCALISATION
#
# for update base: sphinx-build -b gettext . _build/gettext
# for update translations: sphinx-intl update -p _build/gettext -l en_US -l de_DE -l fr_FR -l it_IT -l pt_BR -l es_ES

gettext_uuid = True
gettext_compact = False
