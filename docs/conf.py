"""Configuration file for Sphinx."""
#
# (C) Pywikibot team, 2014-2021
#
# Distributed under the terms of the MIT license.
#
# Pywikibot documentation build configuration file, created by
# sphinx-quickstart on Sun Jun 26 00:00:43 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys

from os.path import abspath, dirname, join

docs_dir = dirname(__file__)
repo_dir = abspath(join(docs_dir, '..'))
sys.path.insert(0, repo_dir)
os.chdir(repo_dir)

os.environ['PYWIKIBOT_NO_USER_CONFIG'] = '1'
import pywikibot  # noqa: E402

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'sphinx.ext.autosummary',
              'sphinx.ext.napoleon']

# Allow lines like "Example:" to be followed by a code block
napoleon_use_admonition_for_examples = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = pywikibot.__name__.title()
project_copyright = pywikibot.__copyright__  # alias since Python 3.5
# author = 'test'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = pywikibot.__version__.partition('.dev')[0]
# The full version, including alpha/beta/rc tags.
release = pywikibot.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# These patterns also affect html_static_path and html_extra_path
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
default_role = 'code'

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
# todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = 'test vtest'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = 'Pywikibot_MW_gear_icon.svg'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs. This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = 'Pywikibot.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = None

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Pywikibotdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'Pywikibot.tex', 'Pywikibot Documentation',
     'Pywikibot team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pywikibot', 'Pywikibot Documentation',
     ['Pywikibot team'], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'Pywikibot', 'Pywikibot Documentation',
     'Pywikibot team', 'Pywikibot', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False


TOKENS_WITH_PARAM = [
    # sphinx
    'param', 'parameter', 'arg', 'argument', 'key', 'keyword',
    'type',
    'raises', 'raise', 'except', 'exception',
    'var', 'ivar', 'cvar',
    'vartype',
    'meta',
    # epytext
    'todo',
]

TOKENS = [
    # sphinx
    'return', 'returns', 'rtype',
    # epytext
    'attention', 'author', 'bug',
    'change', 'changed',
    'contact',
    'copyright', '(c)',
    'deprecated',
    'invariant', 'license', 'note',
    'organization', 'org',
    'permission',
    'postcondition', 'postcond',
    'precondition', 'precond',
    'requires', 'require', 'requirement',
    'see', 'seealso',
    'since', 'status', 'summary', 'todo',
    'version',
    'warn', 'warning',
]


def pywikibot_epytext_to_sphinx(app, what, name, obj, options, lines):
    """Convert epytext tokens to sphinx."""
    result = []
    for line in lines:
        line = re.sub(r'(\A *)@({}) '.format('|'.join(TOKENS_WITH_PARAM)),
                      r'\1:\2 ', line)  # tokens with parameter
        line = re.sub(r'(\A *)@({}):'.format('|'.join(TOKENS)),
                      r'\1:\2:', line)  # short token
        line = re.sub(r'(\A *)@(?:kwarg|kwparam) ',
                      r'\1:keyword ', line)  # keyword
        line = re.sub(r'(\A| )C\{([^}]*)\}', r'\1:py:obj:`\2`', line)  # Link
        line = re.sub(r'(\A| )B\{([^}]*)\}', r'\1**\2**', line)  # Bold
        line = re.sub(r'(\A| )I\{([^}]*)\}', r'\1*\2*', line)  # Italic
        line = re.sub(r'(\A| )C\{([^}]*)\}', r'\1``\2``', line)  # Code
        line = re.sub(r'(\A| )U\{([^}]*)\}', r'\1\2', line)  # Url
        result.append(line)
    lines[:] = result[:]  # assignment required in this way


def pywikibot_script_docstring_fixups(app, what, name, obj, options, lines):
    """Pywikibot specific conversions."""
    from scripts.cosmetic_changes import warning

    if what != 'module':
        return

    if not name.startswith('scripts.'):
        return

    length = 0
    for index, line in enumerate(lines):
        if line == 'Initializer.':
            lines[index] = ''
        elif line == '&params;':
            lines[index] = ('This script supports use of '
                            ':py:mod:`pywikibot.pagegenerators` arguments.')
        elif name == 'scripts.replace' and line == '&fixes-help;':
            lines[index] = ('                  The available fixes are listed '
                            'in :py:mod:`pywikibot.fixes`.')
        elif name == 'scripts.cosmetic_changes' and line == '&warning;':
            lines[index] = warning
        elif name == 'scripts.login' and '*' in line:
            # Escape star wildcard in scripts/login.py
            lines[index] = line.replace('*', '\\*')
        elif (line.endswith(':') and not line.lstrip().startswith(':')
                and 'Traceback (most recent call last)' not in line):
            # Initiate code block except pagegenerator arguments follows
            for afterline in lines[index + 1:]:
                if not afterline:
                    continue
                if afterline != '&params;':
                    lines[index] = line + ':'
                break

        if line.startswith('-'):
            # Indent options
            match = re.match(r'-[^ ]+? +', line)
            if match:
                length = len(match.group(0))
            lines[index] = ' ' + line
        elif length and line.startswith(' ' * length):
            # Indent descriptions of options (as options are indented)
            lines[index] = ' ' + line
        elif line:
            # Reset length
            length = 0

        if '|' in line:
            # Escape vertical bars
            lines[index] = line.replace('|', '\\|')


def pywikibot_skip_members(app, what, name, obj, skip, options):
    """Skip certain members from documentation."""
    inclusions = ()
    exclusions = ()
    if name in inclusions and len(str.splitlines(obj.__doc__ or '')) >= 3:
        return False
    if name.startswith('__') and name.endswith('__'):
        return True
    if obj.__doc__ is not None \
       and ('DEPRECATED' in obj.__doc__ or 'Deprecated' in obj.__doc__):
        return True
    return skip or name in exclusions


def pywikibot_family_classproperty_getattr(obj, name, *defargs):
    """Custom getattr() to get classproperty instances."""
    from sphinx.util.inspect import safe_getattr

    from pywikibot.family import Family
    from pywikibot.tools import classproperty

    if not isinstance(obj, type) or not issubclass(obj, Family):
        return safe_getattr(obj, name, *defargs)

    for base_class in obj.__mro__:
        try:
            prop = base_class.__dict__[name]
        except KeyError:
            continue

        if not isinstance(prop, classproperty):
            return safe_getattr(obj, name, *defargs)

        return prop
    else:
        return safe_getattr(obj, name, *defargs)


def setup(app):
    """Implicit Sphinx extension hook."""
    app.connect('autodoc-process-docstring', pywikibot_epytext_to_sphinx)
    app.connect('autodoc-process-docstring', pywikibot_script_docstring_fixups)
    app.connect('autodoc-skip-member', pywikibot_skip_members)
    app.add_autodoc_attrgetter(type, pywikibot_family_classproperty_getattr)


autoclass_content = 'both'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'special-members': True,
    'show-inheritance': True,
}
