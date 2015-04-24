class TagWeighting:
    def getWeight(self, tag):
        pass

# Some imports have been moved within the code to disconnect this module from the database unless actually required
import math

DEFAULT_FREQ = 10
LOG_SHIFT = 1


class PopularityIdfTagWeighting(TagWeighting):
    def __init__(self, tagRel, popTransform=math.log, idfTransform=math.log, weighted=True, weightsDictionaryPath=None):
        self.weighted = weighted
        self.weightsDict = {}
        if weightsDictionaryPath is not None:
            firstLine = True
            for line in open(weightsDictionaryPath, 'r'):
                if firstLine:
                    firstLine = False
                    continue
                vals = line.strip().split('\t')
                tag = vals[0]
                weight = int(vals[1])
                self.weightsDict[tag] = weight

    def getWeight(self, tag):
        if not self.weighted:
            if self.weightsDict is None:
                return 1
            else:
                return self.weightsDict[tag]
        else:
            return self.popTransform(self.tagEvents.getNumDistinctTaggers(tag)) / self.idfTransform(
                self.docFreqByTag.get(tag, DEFAULT_FREQ) + LOG_SHIFT)
