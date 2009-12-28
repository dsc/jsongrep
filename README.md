# jsongrep - A shell tool to search and select bits out of JSON documents.

jsongrep is a shell tool for extracting values from [JSON](http://json.org) documents. It supports shell-like globbing for property names, and emits the matched values separated by newlines.

Suppose you have a JSON document like the one in `tests/ongz.json` which looks like this:

    {
        "bah" : {
            "feh" : true,
            "foo" : 3,
            "lah" : "songz"
        },
        "blah" : {
            "lol" : "gongz"
        }
    }

jsongrep will let you match structural patterns. Here, we search for all the second-level properties which begin with `l`, provided their first level properties begin with `b`:

    $ jsongrep 'b*.l*' tests/ongz.json
    gongz
    songz

(Heh, the pattern is probably easier to grok than the description.)

jsongrep currently supports normal shell glob patterns within property names:

    ?       Matches any one character
    *       Matches any number of characters within a field
    [seq]   Matches any of the characters in seq
    [!seq]  Matches any of the characters not in seq

Dot is the field separator.


## Installation

jsongrep requires Python >= 2.6. To install:

    $ git clone git://github.com/dsc/jsongrep.git
    $ easy_install jsongrep/setup.py

This will fetch the dependencies and install the script.


## Usage

    Usage: jsongrep [options] [PATTERN | -e PATTERN [-e PATTERN ...]] [FILE]

    Parses JSON data structurally to select a subset of data.

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -e PATTERNS, --pattern=PATTERNS
                            Additional patterns to match.


## TODO

 * Support arrays
 * Support extended regexps
 * Support no-pattern-matching lookup
 * Options:
    * Property separator in patterns (. by default)
    * Output separator (newline by default)
    * Quote string values in output?
    * 1/0 vs true/false for bool values in output?


## Feedback

Open a ticket on github, or send me an email at [dsc@less.ly](mailto:dsc@less.ly).

