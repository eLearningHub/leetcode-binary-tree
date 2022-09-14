"""Sphinx configuration."""
project = "Leetcode Binary Tree"
author = "Behzad Samadi"
copyright = "2022, Behzad Samadi"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
