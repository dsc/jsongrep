#! /usr/bin/env python
from lepl import *
from jsongrep.glob.matchers import *

# from logging import basicConfig, getLogger, DEBUG, INFO
# basicConfig(level=INFO)
# getLogger('lepl.lexer.stream.lexed_simple_stream').setLevel(DEBUG)




# with Separator(sep):

sep      = ~Token('[ \t\.:]')
part     = Token('[^ \t\.:\(\)]+')


char     = Letter() | Digit() | '$' | '_'
idchar   = char | '*' | '?'
numbers  = Digit()[1:,...]
parts    = Delayed()


index    = part( numbers )                          > IndexPart
indexcls = part( Literal('[') & numbers & ']' )
indexpat = (part(numbers | '*' | '?') | indexcls)[1:,...] >> IndexPatternPart


name     = part( Word(char) )                       > NamePart
idcls    = Literal('[') & Word(char) & ']'
idpat    = Word(idchar)
namepat  = part( (idcls | idpat)[1:,...] )          >> NamePatternPart


star     = part('*')                                > StarPart
starstar = part('**')                               > StarStarPart


pat      = Or(
                starstar, star,
                index, indexpat,
                name, namepat
            )
parts   += pat & sep & parts | pat
pattern  = parts | pat                              > Pattern


