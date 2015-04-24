from itemsim.tagweighting import PopularityIdfTagWeighting
from tagrelevance.tagdna import TagDna
from tagrelevance.tagrel import TagRel
from vectorlib.vector import Vector


class TagGenome:
    def __init__(self, tagRel, tagWeighting):
        self.tags = tagRel.getTags()
        self.tagDnas = {}
        for itemId in tagRel.getItems():
            tagRelForItem = tagRel.getTagRelForItem(itemId)
            self.tagDnas[itemId] = TagDna(self,
                                          Vector([tagRelForItem[tag] for tag in self.tags if tag in tagRelForItem]))
        self.weights = map(tagWeighting.getWeight, self.tags)

    def getTags(self):
        return self.tags

    def getTagDna(self, itemId):
        return self.tagDnas[itemId]

    def getTag(self, index):
        return self.tags[index]

    def getWeights(self):
        return self.weights
    
