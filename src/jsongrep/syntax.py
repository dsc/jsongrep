from lepl import *

class Pattern(Node): pass

class Group(Node): pass

class Part(Node): pass

class StarPart(Part): pass

class NamePart(Part): pass

class IndexPart(Part): pass

# class Part(Part): pass


# with Separator(sep):

sep     = ~Token('[ \t\.:]')
part    = Token('[^ \t\.:\(\)]+')


# group   = Delayed()
parts   = Delayed()
pat     = Delayed()



# q1  = Token("'")
# q2  = Token('"')
# quoted  = q1 & Token('[a-zA-Z0-9]') & q1 | q2 & Token() & q2


# star    = part('*') > StarPart

ident   = Letter() | '$' | '_'
name    = part(Word(ident, Star(ident | Digit()))) > NamePart

# index   = Token('[0-9]+') | Token('\[[0-9]+\]') > IndexPart

# pat    += name | star
pat += name


# group   = ~Token('\(') & parts & ~Token('\)') > Group
# parts  += pat & sep & (group | parts | pat)
parts  += pat & sep & (parts | pat)
# pattern = parts | group | pat > Pattern
pattern = (parts | pat) & Eos() > Pattern
