import math


class TagRel:
    def __init__(self, fileName, includeItems=None, subtractTagMean=False, divideByStdDev=False, addPeopleTags=False,
                 normalize=False, testMode=False):

        self.itemTagRelevance = {}
        distinctTags = set()

        if subtractTagMean or divideByStdDev or addPeopleTags:
            tagRelevanceSum = {}
            tagRelevanceCount = {}
            if testMode:
                tagRelevanceData = self._getTagRelevanceData(fileName, addPeopleTags, includeItems)
            else:
                tagRelevanceData = self._getTagRelevanceData(fileName, addPeopleTags)

            for itemId, tag, relevance in tagRelevanceData:
                if normalize:
                    relevance = (relevance - 1) / 4
                if itemId not in self.itemTagRelevance:
                    self.itemTagRelevance[itemId] = {}
                self.itemTagRelevance[itemId][tag] = relevance
                distinctTags.add(tag)
                if tag not in tagRelevanceSum:
                    tagRelevanceSum[tag] = 0.0
                    tagRelevanceCount[tag] = 0
                tagRelevanceSum[tag] += relevance
                tagRelevanceCount[tag] += 1
            if subtractTagMean:
                tagRelevanceMean = dict(
                    [(tag, tagRelevanceSum[tag] / tagRelevanceCount[tag]) for tag in tagRelevanceSum])
                for item in self.itemTagRelevance.keys():
                    self.itemTagRelevance[item] = dict([(tag, relevance - tagRelevanceMean[tag]) for tag, relevance in
                                                          self.itemTagRelevance[item].items()])
            if divideByStdDev:
                tagVarianceSum = {}
                for itemId, tag, relevance in tagRelevanceData:
                    if tag not in tagVarianceSum:
                        tagVarianceSum[tag] = 0.0
                    tagVarianceSum[tag] += (relevance - tagRelevanceMean[tag]) ** 2
                tagRelevanceStdDev = dict(
                    [(tag, math.sqrt(tagVarianceSum[tag] / tagRelevanceCount[tag])) for tag in tagVarianceSum])
                for item in self.itemTagRelevance.keys():
                    self.itemTagRelevance[item] = dict(
                        [(tag, relevance / tagRelevanceStdDev[tag]) for tag, relevance in
                         self.itemTagRelevance[item].items()])
        else:
            # Avoid parsing the first line (header)
            firstLine = True
            if testMode:
                for line in open(fileName):
                    if firstLine:
                        firstLine = False
                        continue
                    vals = line.strip().split('\t')
                    itemId = int(vals[0])
                    if includeItems.count(itemId) > 0:
                        tag = vals[1].replace("\"", "")
                        if vals[2] == 'NA':
                            continue
                        relevance = float(vals[2])
                        if normalize:
                            relevance = (relevance - 1) / 4
                        if itemId not in self.itemTagRelevance:
                            self.itemTagRelevance[itemId] = {}
                        self.itemTagRelevance[itemId][tag] = relevance
                        distinctTags.add(tag)
            else:
                for line in open(fileName):
                    if firstLine:
                        firstLine = False
                        continue
                    vals = line.strip().split('\t')
                    itemId = int(vals[0])
                    tag = vals[1].replace("\"", "")
                    if vals[2] == 'NA':
                        continue
                    relevance = float(vals[2])
                    if normalize:
                        relevance = (relevance - 1) / 4
                    if itemId not in self.itemTagRelevance:
                        self.itemTagRelevance[itemId] = {}
                    self.itemTagRelevance[itemId][tag] = relevance
                    distinctTags.add(tag)

        self.tags = list(distinctTags)
        self.items = self.itemTagRelevance.keys()

    def _getTagRelevanceData(self, fileName, addPeopleTags, includeItems=None):
        tagRelevanceData = []
        firstLine = True
        relItems = set()
        relTags = set()
        if includeItems != None:
            for line in open(fileName):
                if firstLine:
                    firstLine = False
                    continue
                vals = line.strip().split('\t')
                itemId = int(vals[0])
                tag = vals[1].replace("\"", "")
                if vals[2] == 'NA':
                    continue
                if includeItems.count(itemId) > 0:
                    relItems.add(itemId)
                    relTags.add(tag)
                    relevance = float(vals[2])
                    tagRelevanceData.append((itemId, tag, relevance))
        else:
            for line in open(fileName):
                if firstLine:
                    firstLine = False
                    continue
                vals = line.strip().split('\t')
                itemId = int(vals[0])
                tag = vals[1].replace("\"", "")
                if vals[2] == 'NA':
                    continue
                relItems.add(itemId)
                relTags.add(tag)
                relevance = float(vals[2])
                tagRelevanceData.append((itemId, tag, relevance))

        return tagRelevanceData

    def getTagRel(self):
        return self.itemTagRelevance

    def getTagRelForItem(self, itemId, subtractTagMean=False):
        return self.itemTagRelevance[itemId]

    def getTagRelForItemTag(self, itemId, tag):
        try:
            return self.itemTagRelevance[itemId][tag]
        except KeyError:
            return 0

    def getTotalRelByTag(self):
        totalRelByTag = {}
        for tagRelevance in self.itemTagRelevance.values():
            for tag, relevance in tagRelevance.iteritems():
                totalRelByTag[tag] = totalRelByTag.get(tag, 0) + relevance
        return totalRelByTag

    def getDocFreqs(self, threshold=3):
        docFreqsByTag = {}
        for tagRelevance in self.itemTagRelevance.values():
            for tag, relevance in tagRelevance.iteritems():
                if relevance >= threshold:
                    docFreqsByTag[tag] = docFreqsByTag.get(tag, 0) + 1
        return docFreqsByTag

    def getItems(self):
        return self.itemTagRelevance.keys()

    def getTags(self):
        return self.tags

    def getTagRelVector(self, tag):
        return [self.getTagRelForItemTag(itemId, tag) for itemId in self.items]