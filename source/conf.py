# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Add your custom path to sys.path
sys.path.insert(0, os.path.abspath('/proj/xhdsswstaff/preethic/jaanu/my_files'))

project = 'EMBEDDEDSW DOCUMENATION'
copyright = '2025, PREETHI C'
author = 'PREETHI C'
release = '2025.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Automatically document from docstrings
    'sphinx.ext.napoleon',       # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',       # Add links to highlighted source code
    'sphinx.ext.autosummary',    # Generate summary tables
    # Add more extensions if needed
]
templates_path = ['_templates']
exclude_patterns = []

autodoc_mock_imports = ["utils", "build_bsp", "create_app", "open_amp", "validate_bsp"]


language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
