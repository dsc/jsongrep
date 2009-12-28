
def bunchify(d, BunchCls=None):
    "Recursively transforms a dictionary into some flavor of Bunch."
    if not BunchCls:
        BunchCls = Bunch
    return BunchCls( (k, bunchify(v, BunchCls) if isinstance(v, dict) else v) for k,v in d.iteritems() )


class Bunch(dict):
    """ A dictionary that provides attribute-style access.
    """
    
    def __contains__(self, k):
        try:
            return hasattr(self, k) or dict.__contains__(self, k)
        except:
            return False
    
    # only called if k not found in normal places 
    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k)
    
    def __setattr__(self, k, v):
        try:
            # Throws exception if not in prototype chain
            object.__getattribute__(self, k)
            object.__setattr__(self, k, v)
        except:
            try:
                self[k] = v
            except:
                raise AttributeError(k)
    
    def __delattr__(self, k):
        try:
            # Throws exception if not in prototype chain
            object.__getattribute__(self, k)
            object.__delattr__(self, k)
        except:
            try:
                del self[k]
            except KeyError:
                raise AttributeError(k)
    
    def toDict(self):
        c = dict.copy(self)
        for k, v in c.iteritems():
            if callable(getattr(v, 'toDict', None)):
                c[k] = v.toDict()
            elif isinstance(v, dict):
                c[k] = v.copy()
        return c
    
    def __repr__(self):
        keys = self.keys()
        keys.sort()
        args = ', '.join(['%s=%r' % (key, self[key]) for key in keys])
        return '%s(%s)' % (self.__class__.__name__, args)
    
    @staticmethod
    def fromDict(d):
        return bunchify(d, Bunch)


