class TagWeighting:
    def __init__(self):
        pass

    def get_weight(self, tag):
        pass


import math

DEFAULT_FREQ = 10
LOG_SHIFT = 1


class PopularityIdfTagWeighting(TagWeighting):
    def __init__(self, tag_rel, pop_transform=math.log, idf_transform=math.log, weighted=True,
                 weights_dictionary_path=None):
        self.weighted = weighted
        self.weightsDict = {}
        if weights_dictionary_path is not None:
            first_line = True
            for line in open(weights_dictionary_path, 'r'):
                if first_line:
                    first_line = False
                    continue
                values = line.strip().split('\t')
                tag = values[0]
                weight = int(values[1])
                self.weightsDict[tag] = weight

    def get_weight(self, tag):
        if not self.weighted:
            if len(self.weightsDict) == 0:
                return 1
            else:
                return self.weightsDict[tag]
        else:
            print "Added functionality to be added here."
            return 1
