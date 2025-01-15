import sys
import os

sys.path.insert(0, os.path.abspath(os.sep.join((os.curdir, '../..'))))

project = 'BambuLabs API'
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'myst_parser',
              ]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
exclude_patterns = ['_build']
autoclass_content = "both"

html_theme = "sphinx_rtd_theme"
