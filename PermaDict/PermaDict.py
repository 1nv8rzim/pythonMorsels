class PermaDict(dict):
    
    def __init__(self, *args):
        self.permaDict = dict(*args)
        
    def __setitem__(self, key, value):
        if key in self.permaDict:
            raise KeyError(f"'{key}' already in dictionary")
        self.permaDict[key] = value