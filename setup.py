#! python
from setuptools import setup, find_packages

setup(
    name = "jsongrep",
    version = "0.1.1",
    description = "jsongrep Console Tool",
    long_description = """
        Search and select bits out of a JSON document.
    """,
    # url = "http://tire.less.ly/hacking/jsongrep",
    url = "http://github.com/dsc/jsongrep",
    
    author = "David Schoonover",
    author_email = "dsc@less.ly",
    
    packages=['jsongrep', 'jsongrep.glob', 'jsongrep.regexp'],
    zip_safe = True,
    install_requires=[
        "lepl>=3.3.2",
        "bunch>=1.0.0",
        "chardet>=1.0.1",
    ],
    classifiers=[],
    entry_points={
        'console_scripts': ['jsongrep = jsongrep:main']
    },
)
