#!/usr/bin/env python
# encoding: utf-8
__author__    = 'David Schoonover <david@clearspring.com>'
__date__      = '2009-12-24'
__copyright__ = 'Copyright (c) 2009 Clearspring Technologies, Inc. All rights reserved.'
__version__   = (0, 0, 1)

from jsongrep import Pattern, Query


def main():
    from optparse import OptionParser
    
    parser = OptionParser(
        usage   = 'usage: %prog [options] [PATTERN | -e PATTERN [-e PATTERN ...]] [FILE]', 
        description = 'Parses JSON data structurally to select a subset of data.',
        version = '%prog'+" %i.%i.%i" % __version__)
    parser.add_option("-e", "--pattern", action="append", help="Additional patterns to match.")
    parser.add_option("-E", "--regexp", default=Pattern.regexp, action="store_true",
        help="Interpret PATTERN as a Python regular expression. [default: %default]")
    parser.add_option("-s", "--strict", default=Pattern.strict, action="store_true", 
        help="Interpret PATTERN as a bare string, with no pattern matching. [default: %default]")
    parser.add_option("-g", "--glob", default=Pattern.glob, action="store_false",
        help="Interpret PATTERN as a shell-style glob expression. "
             "If specified, overrides --regexp and --strict. [default: %default]")
    parser.add_option("-F", "--field-sep", default=Pattern.field_sep, 
        help="Characters to treat as field-separators delimiting attribute lookups. [default: %default]")
    parser.add_option("-B", "--breadth-first", default=False, action="store_true",
        help="Walks the JSON graph in breadth-first order. [default: %default]")
    parser.add_option("--bools-to-int", dest="bools-to-int", default=False, action="store_true", 
        help="Emit bools as ints (0, 1) instead of names (true, false). [default: %default]")
    parser.add_option("-S", "--out-sep", default=Query.out_sep,
        help="Separator inserted between matches. [default: %default]")
    parser.add_option("-q", "--quote", default=Query.quote, action="store_true",
        help="Adds quotes to matched string values. [default: %default]")
    
    (options, args) = parser.parse_args()
    
    parser.error("incorrect number of arguments")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
