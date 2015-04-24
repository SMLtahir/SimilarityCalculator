class TagDna:
    def __init__(self, tag_genome, rel_vector):
        self.tagGenome = tag_genome
        self.relVector = rel_vector

    def get_rel_vector(self):
        return self.relVector

    def get_description(self, k=None, tag_filter=None, sort_function=lambda x: x):
        if tag_filter:
            value_name = [(rel, self.tagGenome.get_tag(i)) for i, rel in enumerate(self.relVector) if
                          tag_filter.passes(self.tagGenome.get_tag(i))]
        else:
            value_name = [(rel, self.tagGenome.get_tag(i)) for i, rel in enumerate(self.relVector)]
        value_name.sort(key=lambda x: sort_function(x[0]))
        value_name.reverse()
        if k:
            value_name = value_name[0:k]
        return '\n'.join(['%.3f %s' % (val, name) for val, name in value_name])