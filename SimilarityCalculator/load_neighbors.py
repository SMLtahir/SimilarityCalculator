import sys
import os
file_path = os.path.dirname((os.path.abspath(__file__))) + "/"
sys.path.insert(0, file_path)

import argparse
import time
import multiprocessing as mp
import json
import os
import logging

from itemsim.tagdnasim import TagDnaSim
from itemsim.tagweighting import PopularityIdfTagWeighting
from tagrelevance import tagrel
from tagrelevance.taggenome import TagGenome
from vectorlib.kernel import WeightedCosineKernel
from itemsim.neighborhood import Neighborhood


def run():
    global tagDnaSim
    load_configuration()
    load_logger(conf["LOG_NAME"])
    logger.info("LoadNeighbors module starting\nMaking tag_rel object...")
    print "LoadNeighbors module starting\nMaking tag_rel object...", time.strftime('%x %X')

    # Makes a tag_rel object that contains lists of tags, items, an array of itemTagRelevance[itemId] dictionaries
    # that maps a tag to its relevance score for a particular item
    columns = [conf["ITEM1_COLUMN_NO"], conf["ITEM2_COLUMN_NO"], conf["RELEVANCE_SCORE_COLUMN_NO"]]
    relevance_filepath = file_path + conf["FILE_RELEVANCE_PREDICTIONS"]
    tag_rel = tagrel.TagRel(relevance_filepath, columns, field_separator=conf["INPUT_FIELD_SEPARATOR"], normalize=True)
    # For testing purposes use below with desired itemIDs
    # includeItems = [1,4886,6377]
    # tag_rel = tagrel.TagRel(relevance_filepath, includeItems, normalize=True, testMode=True)

    logger.info("Starting tag_weighting...")
    print "Starting tag_weighting...", time.strftime('%x %X')
    # Does a type of tfidf weighting using docFrequencies and number of distinct taggers per tag per item
    weights_filepath = file_path + conf["FILE_TAG_WEIGHTS"]
    if conf["TAG_WEIGHTED"].lower() == 't' or conf["TAG_WEIGHTED"].lower() == 'true' or conf["TAG_WEIGHTED"] \
            .lower() == 'y' or conf["TAG_WEIGHTED"].lower() == 'yes':
        tag_weighting = PopularityIdfTagWeighting(weighted=True, weights_dictionary_path=weights_filepath)
    else:
        tag_weighting = PopularityIdfTagWeighting(weighted=False)

    logger.info("Building tag_genome...")
    print "Building tag_genome...", time.strftime('%x %X')
    # Makes a tag_genome object that contains a list of tags, a map of weights to corresponding tags
    # and a tagDna dictionary that maps every item to its corresponding vector of tag relevance scores
    tag_genome = TagGenome(tag_rel, tag_weighting)

    logger.info("Building kernel_function...")
    print "Building kernel_function...", time.strftime('%x %X')
    # the kernel_function passes weights and two boolean values telling further processes to normalize the weights
    kernel_function = WeightedCosineKernel(tag_genome.get_weights(), True, True)

    logger.info("Building tagDnaSim...")
    print "Building tagDnaSim...", time.strftime('%x %X')
    # Combines the tag_genome and the kernel_function into one object that has methods to compute similarities
    tagDnaSim = TagDnaSim(tag_genome, kernel_function)

    # Get list of items
    global items
    items = tag_rel.get_items()

    logger.info("Writing neighbors and similarities to file...")

    print "Writing neighbors and similarities to file...", time.strftime('%x %X')

    # Write tab separated: itemId, each top neighbor's itemId and similarity value into file
    # Run this in parallel processes
    cpu = conf["NUMBER_OF_CPU"]
    if cpu < 1:
        print "\n\nERROR! NUMBER_OF_CPU config parameter must be set to at least 1.\n\n"
        exit()
    if cpu == "MAX":
        p = mp.Pool(mp.cpu_count())
    else:
        p = mp.Pool(cpu)
    neighbors_filepath = file_path + conf["FILE_NEIGHBORS"]
    with open(neighbors_filepath, 'w') as f:
        for result in p.imap(run_in_parallel, items):
            f.write(result)

    logger.info("LoadNeighbors module successfully completed...")
    print "LoadNeighbors module successfully completed...", time.strftime('%x %X')


def run_in_parallel(item_id):
    n = Neighborhood(item_id)
    n.compute(items, tagDnaSim, size=conf["NEIGHBORHOOD_SIZE"])
    return (
        ''.join(['%d\t%d\t%.4f\n' % (item_id, neighbor, sim) for neighbor, sim in n.get_neighbors_and_sim()]))


def load_configuration():
    global conf
    json_path = file_path + "config/config.json"
    json_conf = open(json_path)
    conf = json.load(json_conf)
    json_conf.close()

    json_test_path = file_path + "config/config.test.json"
    if os.path.exists(json_test_path):
        json_test_conf = open(json_test_path)
        conf_test = json.load(json_test_conf)
        conf.update(conf_test)
        json_test_conf.close()

    json_loc_path = file_path + "config/config.local.json"
    if os.path.exists(json_loc_path):
        json_loc_conf = open(json_loc_path)
        conf_local = json.load(json_loc_conf)
        conf.update(conf_local)
        json_loc_conf.close()


def load_logger(file_name):
    try:
        global logger
        logger = logging.getLogger('| SIM_CALC |')
        logger.setLevel(logging.DEBUG)

        # create file handler for logging
        logfile_path = file_path + file_name
        fh = logging.FileHandler(logfile_path)
        fh.setLevel(logging.INFO)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        logger.addHandler(fh)
        logger.addHandler(ch)
    except IOError, e:
        print 'There was an error logging data into the log file.'
        sys.exit()


def main(argv):
    """ The main() function will be called when the program is run from the command line"""
    parser = argparse.ArgumentParser(
        description='Writes file of item neighbors')
    args = parser.parse_args()
    run()


if __name__ == "__main__":
    main(sys.argv)
