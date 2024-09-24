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

html_logo = 'images/logo.png'

latex_elements = {
    'extraclassoptions': 'openany,oneside',  # 控制文檔的排版選項
    'preamble': r'''
\usepackage{graphicx}  % 引入 graphicx 包以處理圖片
\renewcommand{\maketitle}{
    \begin{flushright}
        \includegraphics[width=0.375\textwidth]{images/logo.png} \\[1cm]  % 插入 logo 圖片
        \Huge \textbf{Tower Semiconductor PH18MKB PDK Documentation} \\[0.5cm]  % 主標題
        \Large \textbf{2023 Latitude Design Systems PTE. LTD.}  % 副標題
    \end{flushright}
}
    ''',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
}
