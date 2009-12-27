#! python
from setuptools import setup, find_packages

setup(
    name = "jsongrep",
    version = "0.0.1",
    description = "Search and select bits out of a JSON document.",
    long_description = """
        Search and select bits out of a JSON document.
    """,
    url = "http://tire.less.ly/hacking/jsongrep",
    
    author = "David Schoonover",
    author_email = "dsc@less.ly",
    
    package_dir = {'':'src'},
    packages=find_packages('src', exclude=['ez_setup']),
    zip_safe = True,
    install_requires=[
        "lepl>=3.3.2",
    ],
    classifiers = [],
)
