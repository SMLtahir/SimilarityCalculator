from similarityfunction import SimilarityFunction


class TagDnaSim(SimilarityFunction):
    def __init__(self, tag_genome, weighted_component_based_kernel):
        self.tagGenome = tag_genome
        self.kernelFunction = weighted_component_based_kernel

    def get_similarity(self, item_id1, item_id2):
        tag_dna1 = self.tagGenome.get_tag_dna(item_id1)
        tag_dna2 = self.tagGenome.get_tag_dna(item_id2)
        return self.kernelFunction.get_sim(tag_dna1.get_rel_vector(), tag_dna2.get_rel_vector())

    def get_similarity_description(self, item_id1, item_id2, num_tags_show=15):
        tag_dna1 = self.tagGenome.get_tag_dna(item_id1)
        tag_dna2 = self.tagGenome.get_tag_dna(item_id2)
        components = self.kernelFunction.get_components_and_weights(tag_dna1.get_rel_vector(), tag_dna2.get_rel_vector())
        components.sort()
        components.reverse()
        sim_detail = [(self.tagGenome.get_tag(i), val, weight) for i, (val, weight) in
                      enumerate(components[0:num_tags_show])]
        return ', '.join(['%s: %.2f(%.2f)' % (tag, val, weight) for tag, val, weight in sim_detail])
