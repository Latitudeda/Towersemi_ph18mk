# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Tower Semiconductor PH18MK PDK Documentation'
copyright = '2023 Latitude Design Systems PTE. LTD.'
author = 'https://www.latitudeds.com/'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
}
