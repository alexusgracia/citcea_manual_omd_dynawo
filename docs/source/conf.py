# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Manual OpenModelica and Dynawo'
copyright = '2025, Joshua Andrew, Miguel Carreño and Alexandre Gràcia, members of CITCEA'
author = 'Joshua Andrew, Miguel Carreño and Alexandre Gràcia, members of CITCEA'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',          # si quieres usar Markdown
    'sphinx.ext.autodoc',   # docstrings automáticos
    'sphinx.ext.napoleon',  # para Google/NumPy docstrings
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
