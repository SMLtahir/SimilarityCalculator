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
                    if len(values) < 2:
                        if len(self.weightsDict) == 0:
                            print "Error! Make sure the weights file is in correct format and that the " \
                                  "field separator is set correctly.\nExiting program."
                            exit()
                        else:
                            print "Warning! Blank line found in weights file. Continuing to next line..."
                            continue
                    tag = values[0]
                    weight = float(values[1])
                    self.weightsDict[tag] = weight
            else:
                print "Error! Please input a path to valid Tag Weights file to continue."
                exit()

    def get_weight(self, tag):
        if self.weighted and tag in self.weightsDict:
            return self.weightsDict[tag]
        else:
            return 1