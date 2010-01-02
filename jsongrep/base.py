# Look for a json parser
try:
    import json
except:
    try:
        import simplejson as json
    except:
        print "jsongrep: your python installation does not appear to have a json parser installed. Try installing simplejson?"
        sys.exit(1)


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
    matches = None
    
    
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
        self.matches = out = []
        
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
    
    def __str__(self):
        if self.matches:
            return '\n'.join( '\n'.join( 
                    json.dumps(m) if isinstance(m, (dict,list)) else str(m) 
                for m in matches ) 
                    for matches in self.matches )
        else:
            return ""


