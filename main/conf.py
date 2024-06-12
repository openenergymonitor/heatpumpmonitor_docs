# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'HeatpumpMonitor'
copyright = '2024, HeatpumpMonitor'
author = 'Trystan'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_copybutton"]
myst_enable_extensions = ["html_image"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']
# include_patterns = ['index.rst','modules/emontx4/docs/*']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "openenergymonitor", # Username
    "github_repo": "heatpumpmonitor_docs", # Repo name
    "github_version": "master", # Version
    "conf_py_path": "/main/", # Path in the checkout to the docs root
}

html_theme_options = {
  'navigation_depth': 3
}
myst_heading_anchors = 3
