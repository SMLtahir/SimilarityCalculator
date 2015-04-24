from similarityfunction import SimilarityFunction


class TagDnaSim(SimilarityFunction):
    def __init__(self, tagGenome, weightedComponentBasedKernel):
        self.tagGenome = tagGenome
        self.kernelFunction = weightedComponentBasedKernel


    def getSimilarity(self, itemId1, itemId2):
        tagDna1 = self.tagGenome.getTagDna(itemId1)
        tagDna2 = self.tagGenome.getTagDna(itemId2)
        return self.kernelFunction.getSim(tagDna1.getRelVector(), tagDna2.getRelVector())

    def getSimilarityDesc(self, itemId1, itemId2, numTagsShow=15):
        tagDna1 = self.tagGenome.getTagDna(itemId1)
        tagDna2 = self.tagGenome.getTagDna(itemId2)
        components = self.kernelFunction.getComponentsAndWeights(tagDna1.getRelVector(), tagDna2.getRelVector())
        components.sort()
        components.reverse()
        simDetail = [(self.tagGenome.getTag(i), val , weight) for i, (val, weight) in enumerate(components[0:numTagsShow])]
        return ', '.join(['%s: %.2f(%.2f)'%(tag, val, weight) for tag, val, weight in simDetail])
