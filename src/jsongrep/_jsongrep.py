


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
        
        return out
    

class Query(object):
    """ Applies a pattern to JSON data, returning the result. """
    
    
    def __init__(self, patterns, data):
        self.patterns = patterns
        self.data = data
    







