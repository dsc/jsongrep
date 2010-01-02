from fnmatch import fnmatchcase
from jsongrep.matchers import Part, Pattern



class NamePart(Part):
    "Matches given name, no funny business."
    
    def matchDict(self, data, nextpat):
        return [ data[self.content] ] if self.content in data else []
    


class NamePatternPart(Part):
    "Matches a given name pattern."
    
    def matchDict(self, data, nextpat):
        return [ data[k] for k in data if fnmatchcase(k, self.content) ]
    
    def matchList(self, data, nextpat):
        return [ data[i] for i in xrange(len(data)) if fnmatchcase(str(i), self.content) ]


class IndexPart(Part):
    "Matches an array by index."
    
    def matchList(self, data, nextpat):
        idx = int(self.content)
        return [ data[idx] ] if idx < len(data) else []

class IndexPatternPart(Part):
    "Matches an array by index pattern."
    
    def matchList(self, data, nextpat):
        return [ data[i] for i in xrange(len(data)) if fnmatchcase(str(i), self.content) ]


# class Part(Part): pass

class StarPart(Part):
    "Matches any name"
    
    def matchList(self, data, nextpat):
        return data[:]
    
    def matchDict(self, data, nextpat):
        return [ data[k] for k in data ]
    

class StarStarPart(Part):
    def matchList(self, data, nextpat):
        return data[:]
    
    def matchDict(self, data, nextpat):
        return [ data[k] for k in data ]
    





