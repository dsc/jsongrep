jsongrep is a shell tool for extracting values from JSON documents. It supports shell-like globbing for property names, and emits the matched values separated by newlines.


Examples
--------

Let's start with a real-world example.

Let's grab the even tweets from the last 10 pulled from Twitter's JSON feed http://apiwiki.twitter.com/Twitter-REST-API-Method:-statuses-public_timeline ::

    $ curl -s 'http://twitter.com/statuses/public_timeline.json' | jsongrep '[02468].text'
    ARGHHHHHH. facebook is being gay
    5-5 in the darts between Barney and Whitlock. Amazing. #darts
    I wonder if I'm still located on 5th ave?
    Estou de volta  a internet .... Essa chuva n para !   Estou de boa com a minha familia .

Yeah, that's just about what I expected.

Now suppose you have a JSON document like the one in ``tests/ongz.json`` which looks like this::

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

jsongrep will let you match structural patterns, where ``.`` (dot) separates nested properties.

Let's glob on property names::

    $ jsongrep 'b*.l*' tests/ongz.json
    gongz
    songz

Works on arrays, too::

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

Note that we're still globbing, even though arrays have numeric indices::

    $ jsongrep 'arr.2?' tests/ongz.json
    u
    v
    w
    x
    y
    z

If you specify a JSON subtree, that's what you get back::

    $ jsongrep 'bah' tests/ongz.json
    {"foo": 3, "lah": "songz", "feh": true}


Syntax
------

jsongrep currently supports normal shell glob patterns within property names::

    ?       Matches any one character
    *       Matches any number of characters within a field
    [seq]   Matches any of the characters in seq
    [!seq]  Matches any of the characters not in seq

Dot is the field separator.


Usage
-----

::

    Usage: jsongrep [options] [PATTERN | -e PATTERN [-e PATTERN ...]] [FILE]

    Parses JSON data structurally to select a subset of data.

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -e PATTERNS, --pattern=PATTERNS
                            Additional patterns to match.
      -D, --detect-encoding
                            Attempts to detect the character encoding of input if
                            LC_TYPE and file.encoding provide insufficient hints.
                            (Slow) [default: False]


TODO
----

* Support star-star (``**``) non-greedy matches of spanning subgraphs
* Support unicode, escapes in patterns
* Support extended regexps
* Support no-pattern-matching lookup
* Options:
    * Property separator in patterns (. by default)
    * Output separator (newline by default)
    * Quote string values in output?
    * 1/0 vs true/false for bool values in output?


Feedback
--------

Open a ticket at http://github.com/dsc/jsongrep , or send me an email at dsc@less.ly .

