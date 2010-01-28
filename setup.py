#! python
import os
from setuptools import setup

version = "0.1.1"

# Read the long description from the README.txt
here = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(here, 'docs/README.rst'))
readme = f.read()
f.close()


setup(
    name = "jsongrep",
    packages=['jsongrep', 'jsongrep.glob', 'jsongrep.regexp'],
    description = "Search and select bits out of a JSON document.",
    version = version,
    author = "David Schoonover",
    author_email = "dsc@less.ly",
    long_description = readme,
    url = "http://tire.less.ly/hacking/jsongrep",
    download_url = "http://pypi.python.org/packages/source/j/jsongrep/jsongrep-%s.tar.gz" % version,
    keywords = ['jsongrep', 'json', 'grep', 'search', 'console', 'cli', 'shell'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
    install_requires=[
        "lepl>=3.3.2",
        "bunch>=1.0.0",
        "chardet>=1.0.1",
    ],
    entry_points={
        'console_scripts': ['jsongrep = jsongrep:main']
    },
    license = 'MIT',
    zip_safe = True,
)
