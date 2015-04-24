# Represents the neighborhood of a item


class Neighborhood():
    def __init__(self, itemId, neighborSimilarity=None):
        self.itemId = itemId
        self.neighborSimilarity = neighborSimilarity

    def compute(self, allItems, similarityFunction, minSimilarity=None, size=None):
        assert minSimilarity == None or size == None, 'Must choose neighborhood based on size or similarity'
        self.similarityFunction = similarityFunction
        similarities = dict(
            [(itemId, similarityFunction.getSimilarity(self.itemId, itemId))
             for itemId in allItems])
        if size != None:
            sorter = [(similarity, itemId) for itemId, similarity in similarities.iteritems()]
            sorter.sort()
            sorter.reverse()
            self.neighborSimilarity = dict([(itemId, similarity) for similarity, itemId in sorter[0:size]])
        elif minSimilarity != None:
            self.neighborSimilarity = dict([(itemId, similarity) for itemId, similarity in similarities.iteritems()
                                            if similarity >= minSimilarity])
        else:
            self.neighborSimilarity = similarities

    def getNeighbors(self):
        sorter = [(similarity, itemId) for itemId, similarity in self.neighborSimilarity.iteritems()]
        sorter.sort()
        sorter.reverse()
        return zip(*sorter)[1]

    def getNeighborsAndSim(self):
        sorter = [(similarity, itemId) for itemId, similarity in self.neighborSimilarity.iteritems()]
        sorter.sort()
        sorter.reverse()
        return [(itemId, similarity) for similarity, itemId in sorter]

    def getNumNeighbors(self):
        return len(self.neighborSimilarity)

    def getSimilarity(self, neighbor):
        return self.neighborSimilarity[neighbor]

    def getSimilarityDesc(self, neighbor):
        return self.similarityFunction.getSimilarityDesc(self.itemId, neighbor)