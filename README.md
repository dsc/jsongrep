# jsongrep - A shell tool to search and select bits out of JSON documents.

jsongrep is a shell tool for extracting values from [JSON](http://json.org) documents. It supports shell-like globbing for property names, and emits the matched values separated by newlines.


## Examples

Let's start with a real-world example.

Let's grab the even tweets from the last 10 pulled from Twitter's JSON feed:

    $ curl -s 'http://twitter.com/statuses/public_timeline.json' | jsongrep '[02468].text'
    それでｒはみなさｌあごきげんよい
    ARGHHHHHH. facebook is being gay
    5-5 in the darts between Barney and Whitlock. Amazing. #darts
    I wonder if I'm still located on 5th ave?
    Estou de volta  a internet .... Essa chuva ñ para !   Estou de boa com a minha familia .

Yeah, that's just about what I expected.

Now suppose you have a JSON document like the one in `tests/ongz.json` which looks like this:

    {
        "bah" : {
            "feh" : true,
            "foo" : 3,
            "lah" : "songz"
        },
        "blah" : {
            "lol" : "gongz"
        },
        "arr" : [
            "a", "b", "c", "d", "e", 
            "f", "g", "h", "i", "j", 
            "k", "l", "m", "n", "o", 
            "p", "q", "r", "s", "t", 
            "u", "v", "w", "x", "y", 
            "z"
        ]
    }

jsongrep will let you match structural patterns, where `.` (dot) separates nested properties. 

Let's glob on property names:

    $ jsongrep 'b*.l*' tests/ongz.json
    gongz
    songz

Works on arrays, too:

    $ jsongrep 'arr.?' tests/ongz.json
    a
    b
    c
    d
    e
    f
    g
    h
    i
    j

Note that we're still globbing, even though arrays have numeric indices:

    jsongrep 'arr.2?' tests/ongz.json
    u
    v
    w
    x
    y
    z

If you specify a JSON subtree, that's what you get back.

    $ jsongrep 'bah' tests/ongz.json 
    {"foo": 3, "lah": "songz", "feh": true}


## Syntax

jsongrep currently supports normal shell glob patterns within property names:

    ?       Matches any one character
    *       Matches any number of characters within a field
    [seq]   Matches any of the characters in seq
    [!seq]  Matches any of the characters not in seq

Dot is the field separator.


## Installation

jsongrep requires Python >= 2.6. To install:

    $ git clone git://github.com/dsc/jsongrep.git
    $ easy_install jsongrep

Or if you have [pip](http://pip.openplans.org/) installed:

    $ pip install -e git://github.com/dsc/jsongrep.git#egg=jsongrep

Both will fetch the dependencies and install the script.


## Usage

    Usage: jsongrep [options] [PATTERN | -e PATTERN [-e PATTERN ...]] [FILE]

    Parses JSON data structurally to select a subset of data.

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -e PATTERNS, --pattern=PATTERNS
                            Additional patterns to match.


## TODO

 * Support star-star (`**`) non-greedy matches of spanning subgraphs
 * Support unicode, escapes in patterns
 * Support extended regexps
 * Support no-pattern-matching lookup
 * Options:
    * Property separator in patterns (. by default)
    * Output separator (newline by default)
    * Quote string values in output?
    * 1/0 vs true/false for bool values in output?


## Feedback

Open a ticket on github, or send me an email at [dsc@less.ly](mailto:dsc@less.ly).

