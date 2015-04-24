class TagDna:
    def __init__(self, tagGenome, relVector):
        self.tagGenome = tagGenome
        self.relVector = relVector
    def getRelVector(self):
        return self.relVector
    def getDesc(self, k=None, tagFilter=None, sortFunction = lambda x:x):
        if tagFilter:
            valName = [(rel, self.tagGenome.getTag(i)) for i, rel in enumerate(self.relVector) if tagFilter.passes(self.tagGenome.getTag(i))]
        else:
            valName = [(rel, self.tagGenome.getTag(i)) for i, rel in enumerate(self.relVector)]
        valName.sort(key = lambda x:sortFunction(x[0]))
        valName.reverse()
        if k:
            valName = valName[0:k]
        return '\n'.join(['%.3f %s'%(val,name) for val,name in valName])