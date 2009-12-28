#!/usr/bin/env python
# encoding: utf-8
__author__    = 'David Schoonover <david@clearspring.com>'
__date__      = '2009-12-24'
__copyright__ = 'Copyright (c) 2009 Clearspring Technologies, Inc. All rights reserved.'
__version__   = (0, 0, 1)

import sys, os, os.path, json
from jsongrep.util.bunch import Bunch

class JSONGrepOptions(Bunch):
    "Options parser for jsongrep."
    DEFAULTS = {
        'glob'      : True,
        'regexp'    : False,
        'strict'    : False,
        'field_sep' : '.: ',
        'splitter'  : None,
        'out_sep'   : '\n',
        'quote'     : False,
        
        'patterns'  : None,
        'file'      : None,
    }
    
    def __init__(self, *args, **options):
        self.update(JSONGrepOptions.DEFAULTS.copy())
        self.patterns = []
        options = Bunch.fromDict(options)
        
        self.update(options)
        
        # if self.glob:
        #     self.regexp = self.strict = False
        # elif self.regexp:
        #     self.glob = self.strict = False
        # elif self.strict:
        #     self.glob = self.regexp = False
        # else:
        #     self.glob = True
        #     self.regexp = self.strict = False
        # 
        if not args:
            self.file = sys.stdin
        elif len(args) > 2:
            raise ValueError("Too many arguments!")
        elif len(args) == 2:
            pattern, file = args
            self.patterns.insert(0, pattern)
            self.file = open(file, 'rU')
        elif args:
            first = args[0]
            if os.path.exists(first):
                self.file = open(first, 'rU')
            else:
                self.patterns.insert(0, first)
                self.file = sys.stdin
        
        if not self.patterns:
            raise ValueError('No patterns supplied!')
        
    

class JSONGrep(object):
    """Programmatic entrypoint."""
    options = None
    patterns = []
    file = None
    json = None
    
    
    def __init__(self, patterns=None, file=None, options=None):
        self.options = Bunch.fromDict(options or {})
        self.file = file or options.get('file', None)
        self.patterns = patterns or options.patterns or []
    
    def compile(self, pats=None):
        from jsongrep.glob import pattern
        # TODO: trap lepl errors
        self.patterns = [ pattern.parse(pat)[0] for pat in (pats or self.patterns) ]
        return self.patterns
    
    def process(self, fp=None):
        self.json = json.load(fp or self.file)
        matches = [self.json]
        out = []
        
        # print 'patterns:', self.patterns
        for pattern in self.patterns:
            # print '--> pattern:\n', pattern
            for part in pattern:
                nextpat = pattern.nextFrom(part)
                # print '... pattern=%r, nextpat=%r' % (part, nextpat)
                _current = matches[:]
                matches = []
                for data in _current:
                    m = part.match(data, nextpat)
                    # print '... --> matches:', m
                    if m: matches += m
                if not matches:
                    break
            out.append( matches )
        return out



def main():
    from optparse import OptionParser
    DEFAULTS = JSONGrepOptions.DEFAULTS
    
    parser = OptionParser(
        usage   = 'usage: %prog [options] [PATTERN | -e PATTERN [-e PATTERN ...]] [FILE]', 
        description = 'Parses JSON data structurally to select a subset of data.',
        version = '%prog'+" %i.%i.%i" % __version__)
    parser.add_option("-e", "--pattern", action="append", dest="patterns", help="Additional patterns to match.")
    # parser.add_option("-E", "--regexp", default=Pattern.regexp, action="store_true",
    #     help="Interpret PATTERN as a Python regular expression. [default: %default]")
    # parser.add_option("-s", "--strict", default=Pattern.strict, action="store_true", 
    #     help="Interpret PATTERN as a bare string, with no pattern matching. [default: %default]")
    # # TODO: glob, regex, strict to be mutually exclusive
    # parser.add_option("-g", "--glob", default=None, action="store_false",
    #     help="Interpret PATTERN as a shell-style glob expression. "
    #          "If specified, overrides --regexp and --strict. [default: %default]")
    # parser.add_option("-F", "--field-sep", default=Pattern.field_sep, 
    #     help="Characters to treat as field-separators delimiting attribute lookups. [default: %default]")
    # parser.add_option("-B", "--breadth-first", default=False, action="store_true",
    #     help="Walks the JSON graph in breadth-first order. [default: %default]")
    # parser.add_option("--bools-to-int", dest="bools-to-int", default=False, action="store_true", 
    #     help="Emit bools as ints (0, 1) instead of names (true, false). [default: %default]")
    # parser.add_option("-S", "--out-sep", default=Query.out_sep,
    #     help="Separator inserted between matches. [default: %default]")
    # parser.add_option("-q", "--quote", default=Query.quote, action="store_true",
    #     help="Adds quotes to matched string values. [default: %default]")
    
    (options, args) = parser.parse_args()
    
    try:
        opts = JSONGrepOptions(*args, **options.__dict__)
    except ValueError as e:
        parser.error(e.msg)
        return 1
    
    grep = JSONGrep(options=opts)
    grep.compile()
    print '\n'.join( '\n'.join(matches) for matches in grep.process() )
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
