from itemsim.tagweighting import PopularityIdfTagWeighting
from tagrelevance.tagdna import TagDna
from tagrelevance.tagrel import TagRel
from vectorlib.vector import Vector


class TagGenome:
    def __init__(self, tag_rel, tag_weighting):
        self.tags = tag_rel.get_tags()
        self.tag_dnas = {}
        for itemId in tag_rel.get_items():
            tag_rel_for_item = tag_rel.get_tag_rel_for_item(itemId)
            self.tag_dnas[itemId] = TagDna(self, Vector(
                [tag_rel_for_item[tag] for tag in self.tags if tag in tag_rel_for_item]))
        self.weights = map(tag_weighting.get_weight, self.tags)

    def get_tags(self):
        return self.tags

    def get_tag_dna(self, item_id):
        return self.tag_dnas[item_id]

    def get_tag(self, index):
        return self.tags[index]

    def get_weights(self):
        return self.weights