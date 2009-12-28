#! /usr/bin/env python
from lepl import *
from jsongrep.regexp.matchers import *

# from logging import basicConfig, getLogger, DEBUG, INFO
# basicConfig(level=INFO)
# getLogger('lepl.lexer.stream.lexed_simple_stream').setLevel(DEBUG)




# with Separator(sep):

sep      = ~Token('[ \t\.:]')
part     = Token('[^ \t\.:\(\)]+')


group    = Delayed()
parts    = Delayed()
# pat      = Delayed()



# q1  = Token("'")
# q2  = Token('"')
# quoted  = q1 & Token('[a-zA-Z0-9]') & q1 | q2 & Token() & q2


star     = part('*') > StarPart
starstar = part('**') > StarStarPart


name_hd  = Letter() | '$' | '_'
name_tl  = name_hd | Digit()
name     = part(Word( name_hd, name_tl )) > NamePart

idclass  = Literal('[') & Word(name_tl) & ']'
idpat_hd = name_hd | '*' | '?'
idpat_tl = name_tl | '*' | '?'
idpat    = Word(idpat_hd, idpat_tl)
namepat  = part( (idclass | idpat)[1:,...] ) >> NamePatternPart

# index  = Token('[0-9]+') | Token('\[[0-9]+\]') > IndexPart

pat      = starstar | star | name | namepat


group    = ~Token('\(') & parts & ~Token('\)') > Group
parts   += pat & sep & (group | parts | pat)
# parts   += pat & sep & parts | pat
pattern  = parts | group | pat > Pattern
# pattern  = parts | pat > Pattern


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = 'f?o*?o.*.([09].(**.baz))'
    print "arg=%s" % arg
    print pattern.parse(arg)[0]
