# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pyVoIP'
copyright = '2025, Jose Acevedo'
author = 'Jose Acevedo'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
 'sphinx.ext.autodoc',
 'sphinx.ext.napoleon',         # para docstrings estilo Google / NumPy
 'sphinx.ext.autosummary',
 'sphinx_autodoc_typehints',
 'sphinx.ext.viewcode',
 ]

import os
import sys
sys.path.insert(0, os.path.abspath('/Users/joseacevedo/Documents/GitHub/ie-0417/Lab2/pyVoIP'))

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
