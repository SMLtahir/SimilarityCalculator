# Represents the neighborhood of a item


class Neighborhood():
    def __init__(self, item_id, neighbor_similarity=None):
        self.itemId = item_id
        self.neighborSimilarity = neighbor_similarity

    def compute(self, all_items, similarity_function, min_similarity=None, size=None):
        assert min_similarity is None or size is None, 'Must choose neighborhood based on size or similarity'
        self.similarity_function = similarity_function
        similarities = dict(
            [(itemId, similarity_function.get_similarity(self.itemId, itemId))
             for itemId in all_items])
        if size is not None:
            sorter = [(similarity, itemId) for itemId, similarity in similarities.iteritems()]
            sorter.sort()
            sorter.reverse()
            self.neighborSimilarity = dict([(itemId, similarity) for similarity, itemId in sorter[0:size]])
        elif min_similarity is not None:
            self.neighborSimilarity = dict([(itemId, similarity) for itemId, similarity in similarities.iteritems()
                                            if similarity >= min_similarity])
        else:
            self.neighborSimilarity = similarities

    def get_neighbors(self):
        sorter = [(similarity, itemId) for itemId, similarity in self.neighborSimilarity.iteritems()]
        sorter.sort()
        sorter.reverse()
        return zip(*sorter)[1]

    def get_neighbors_and_sim(self):
        sorter = [(similarity, itemId) for itemId, similarity in self.neighborSimilarity.iteritems()]
        sorter.sort()
        sorter.reverse()
        return [(itemId, similarity) for similarity, itemId in sorter]

    def get_num_neighbors(self):
        return len(self.neighborSimilarity)

    def get_similarity(self, neighbor):
        return self.neighborSimilarity[neighbor]

    def get_similarity_description(self, neighbor):
        return self.similarity_function.get_similarity_description(self.itemId, neighbor)