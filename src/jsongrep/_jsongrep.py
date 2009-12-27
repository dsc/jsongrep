import sys, re, fnmatch

SPLIT_PREFIX = r'(?<!\\)'
STRIP_PAT = r'\\'
IS_BE_DIGITZ = re.compile(r'^\[\d+\]$').search
IS_BE_ALL_QZ = re.compile(r'^\?+$').search

class Match(object):
    """ Represents one of the many match-types in a pattern. 
        
        I'd use a recursive decent parser framework like antlr or lepl, 
        but I don't want to introduce dependencies.
    """
    def __init__(self, part):
        self.part = part
    
    def match(self, data):
        pass
    

class IntMatch(Match):
    """Matches an index into an array (or a numeric object property, feh)."""
    
    def match(self, data):
        pass
    

class ArrayMatch(IntMatch):
    """Matches an index into an array."""
    
    def match(self, data):
        pass

class GroupingMatch(Match):
    

class PropertyMatch(Match):
    




class Pattern(object):
    """ Represents a query pattern. """
    pattern   = None
    glob      = True
    regexp    = False
    strict    = False
    field_sep = '.: '
    
    splitter  = None
    
    
    def __init__(self, pattern, **options):
        for k, v in options.iteritems():
            if hasattr(self, k):
                setattr(self, k, v)
        self.compile(pattern)
    
    def compile(self, pattern):
        self.splitter = re.compile( r'(?<!\\)[%s]' % re.escape(self.field_sep) ).split
        self.pattern = pattern
        self.parts = []
        for part in self.splitter(pattern):
            try:
                part = int(part)
            except ValueError: pass
            if IS_BE_DIGITZ(part):
                part = map(int, part[1:-1]) # TODO: create a dummy _intMatch
            self.parts.append(part)
    
    def _intMatcher(i):
        
        def intMatch(data):
            
    
    def _intGroupMatcher(part):
        
    
    def match(self, data, parts=None, part=None):
        "Returns a list of matches"
        out = []
        parts = parts or self.parts
        
        if parts is None and part is None:
            return [ data ]
        
        if isinstance(data, list):
            if part is None:
                part, parts = parts[0], parts[1:]
            
            if isinstance(part, int) and part < len(data):
                out += self.match(data[part], parts)
            elif isinstance(part, list):
                for p in part:
                    out += self.match(data, parts, p)
            elif part == '*':
                for v in data:
                    out += self.match(v, parts)
            elif IS_BE_ALL_QZ(part):
                for v in data[:(10 * len(part))]:
                    out += self.match(v, parts)
            # todo: [!...]
        elif isinstance(data, dict):
            if 
        
        return out
    

class Query(object):
    """ Applies a pattern to JSON data, returning the result. """
    out_sep   = '\n'
    quote     = False
    
    
    def __init__(self, patterns, data):
        self.patterns = patterns
        self.data = data
    







