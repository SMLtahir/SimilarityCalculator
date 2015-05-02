class TagWeighting:
    def __init__(self):
        pass

    def get_weight(self, tag):
        pass


class PopularityIdfTagWeighting(TagWeighting):
    def __init__(self, weighted=False, weights_dictionary_path=None):
        self.weighted = weighted
        self.weightsDict = {}
        if not self.weighted:
            print "All tags will be equally weighted."
        else:
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
            else:
                print "Error! Please input a path to valid Tag Weights file to continue."
                exit()

    def get_weight(self, tag):
        if self.weighted:
            return self.weightsDict[tag]
        else:
            return 1