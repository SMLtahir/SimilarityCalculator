import math


class TagRel:
    def __init__(self, file_name, field_separator='\t', include_items=None, subtract_tag_mean=False,
                 divide_by_std_dev=False, add_people_tags=False, normalize=False, test_mode=False):

        self.itemTagRelevance = {}
        distinct_tags = set()

        if subtract_tag_mean or divide_by_std_dev or add_people_tags:
            tag_relevance_sum = {}
            tag_relevance_count = {}
            if test_mode:
                tag_relevance_data = self._get_tag_relevance_data(file_name, add_people_tags, include_items,
                                                                  field_separator=field_separator)
            else:
                tag_relevance_data = self._get_tag_relevance_data(file_name, add_people_tags,
                                                                  field_separator=field_separator)

            for item_id, tag, relevance in tag_relevance_data:
                if normalize:
                    relevance = (relevance - 1) / 4
                if item_id not in self.itemTagRelevance:
                    self.itemTagRelevance[item_id] = {}
                self.itemTagRelevance[item_id][tag] = relevance
                distinct_tags.add(tag)
                if tag not in tag_relevance_sum:
                    tag_relevance_sum[tag] = 0.0
                    tag_relevance_count[tag] = 0
                tag_relevance_sum[tag] += relevance
                tag_relevance_count[tag] += 1
            if subtract_tag_mean:
                tag_relevance_mean = dict(
                    [(tag, tag_relevance_sum[tag] / tag_relevance_count[tag]) for tag in tag_relevance_sum])
                for item in self.itemTagRelevance.keys():
                    self.itemTagRelevance[item] = dict([(tag, relevance - tag_relevance_mean[tag]) for tag, relevance in
                                                        self.itemTagRelevance[item].items()])
            if divide_by_std_dev:
                tag_variance_sum = {}
                for item_id, tag, relevance in tag_relevance_data:
                    if tag not in tag_variance_sum:
                        tag_variance_sum[tag] = 0.0
                    tag_variance_sum[tag] += (relevance - tag_relevance_mean[tag]) ** 2
                tag_relevance_std_dev = dict(
                    [(tag, math.sqrt(tag_variance_sum[tag] / tag_relevance_count[tag])) for tag in tag_variance_sum])
                for item in self.itemTagRelevance.keys():
                    self.itemTagRelevance[item] = dict(
                        [(tag, relevance / tag_relevance_std_dev[tag]) for tag, relevance in
                         self.itemTagRelevance[item].items()])
        else:
            # Avoid parsing the first line (file header)
            first_line = True
            if test_mode:
                for line in open(file_name):
                    if first_line:
                        first_line = False
                        continue
                    values = line.strip().split(field_separator)
                    item_id = int(values[0])
                    if include_items.count(item_id) > 0:
                        tag = values[1].replace("\"", "")
                        if values[2] == 'NA':
                            continue
                        relevance = float(values[2])
                        if normalize:
                            relevance = (relevance - 1) / 4
                        if item_id not in self.itemTagRelevance:
                            self.itemTagRelevance[item_id] = {}
                        self.itemTagRelevance[item_id][tag] = relevance
                        distinct_tags.add(tag)
            else:
                for line in open(file_name):
                    if first_line:
                        first_line = False
                        continue
                    values = line.strip().split(field_separator)
                    item_id = int(values[0])
                    tag = values[1].replace("\"", "")
                    if values[2] == 'NA':
                        continue
                    relevance = float(values[2])
                    if normalize:
                        relevance = (relevance - 1) / 4
                    if item_id not in self.itemTagRelevance:
                        self.itemTagRelevance[item_id] = {}
                    self.itemTagRelevance[item_id][tag] = relevance
                    distinct_tags.add(tag)

        self.tags = list(distinct_tags)
        self.items = self.itemTagRelevance.keys()

    def _get_tag_relevance_data(self, file_name, field_separator='\t', include_items=None):
        tag_relevance_data = []
        first_line = True
        rel_items = set()
        rel_tags = set()
        if include_items is not None:
            for line in open(file_name):
                if first_line:
                    first_line = False
                    continue
                values = line.strip().split(field_separator)
                item_id = int(values[0])
                tag = values[1].replace("\"", "")
                if values[2] == 'NA':
                    continue
                if include_items.count(item_id) > 0:
                    rel_items.add(item_id)
                    rel_tags.add(tag)
                    relevance = float(values[2])
                    tag_relevance_data.append((item_id, tag, relevance))
        else:
            for line in open(file_name):
                if first_line:
                    first_line = False
                    continue
                values = line.strip().split(field_separator)
                item_id = int(values[0])
                tag = values[1].replace("\"", "")
                if values[2] == 'NA':
                    continue
                rel_items.add(item_id)
                rel_tags.add(tag)
                relevance = float(values[2])
                tag_relevance_data.append((item_id, tag, relevance))

        return tag_relevance_data

    def get_tag_rel(self):
        return self.itemTagRelevance

    def get_tag_rel_for_item(self, item_id):
        return self.itemTagRelevance[item_id]

    def get_tag_rel_for_item_tag(self, item_id, tag):
        try:
            return self.itemTagRelevance[item_id][tag]
        except KeyError:
            return 0

    def get_total_rel_by_tag(self):
        total_rel_by_tag = {}
        for tagRelevance in self.itemTagRelevance.values():
            for tag, relevance in tagRelevance.iteritems():
                total_rel_by_tag[tag] = total_rel_by_tag.get(tag, 0) + relevance
        return total_rel_by_tag

    def get_doc_frequencies(self, threshold=3):
        doc_frequencies_by_tag = {}
        for tagRelevance in self.itemTagRelevance.values():
            for tag, relevance in tagRelevance.iteritems():
                if relevance >= threshold:
                    doc_frequencies_by_tag[tag] = doc_frequencies_by_tag.get(tag, 0) + 1
        return doc_frequencies_by_tag

    def get_items(self):
        return self.itemTagRelevance.keys()

    def get_tags(self):
        return self.tags

    def get_tag_rel_vector(self, tag):
        return [self.get_tag_rel_for_item_tag(itemId, tag) for itemId in self.items]