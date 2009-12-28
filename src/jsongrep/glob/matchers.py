from lepl import Node
from fnmatch import fnmatchcase


class Part(Node):
    
    @property
    def content(self):
        return self[0]
    
    def match(self, data, nextpat):
        "Returns the collection of matching sub-objects which match this pattern part or None."
        if not data:
            return []
        elif isinstance(data, list):
            return self.matchList(data, nextpat)
        elif isinstance(data, dict):
            return self.matchDict(data, nextpat)
        elif nextpat is None:
            return [ data ]
        else:
            return []
    
    def matchList(self, data, nextpat):
        return []
    
    def matchDict(self, data, nextpat):
        return []



class NamePart(Part):
    def matchDict(self, data, nextpat):
        return [ data[self.content] ] if self.content in data else []
    


class NamePatternPart(Part):
    def matchDict(self, data, nextpat):
        return [ data[k] for k in data if fnmatchcase(k, self.content) ]
    

# class IndexPart(Part): pass
# class Part(Part): pass

class StarPart(Part):
    def matchList(self, data, nextpat):
        return data[:]
    
    def matchDict(self, data, nextpat):
        return [ data[k] for k in data ]
    

class StarStarPart(Part):
    def matchList(self, data, nextpat):
        return data[:]
    
    def matchDict(self, data, nextpat):
        return [ data[k] for k in data ]
    





class Pattern(Node):
    
    def iterFrom(self, start=None):
        "Iterates over the pattern tree. If a node is supplied, starts iterating after that node."
        parent = iter(self)
        parents = [[]]
        child = None
        foundStart = start is None
        while parents:
            try:
                child = parent.next()
            except StopIteration:
                if parents:
                    parent = iter(parents.pop())
                    continue
                else:
                    break
            
            if foundStart:
                yield child
            elif start is child:
                foundStart = True
            
            if isinstance(child, Node):
                parents.append(parent)
                parent = iter(child)
        
    
    def nextFrom(self, current):
        "Returns the next pattern from a node or None if last."
        return next(self.iterFrom(current), None)
    



