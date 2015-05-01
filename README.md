# SimilarityCalculator

*Python open source package that computes similarities between a list of items based on their tag relevance scores 
and prints the top neighbors of each item to file.* 

##### Travis CI Testing status 

[![Build Status](https://travis-ci.org/SMLtahir/SimilarityCalculator.svg?branch=master)](https://travis-ci.org/SMLtahir/SimilarityCalculator)

##### Set **PYTHONPATH** environment variable to your Python bin directory

##### Set **SIMCALC_HOME** in config.local.json:
In SimilarityCalculator/config/ directory, create file config.local.json and paste,

```
{

        "SIMCALC_HOME": "<ROOT_DIRECTORY_OF_SimilarityCalculator>"
}
```

If the file was already created and there are more entries, add a comma followed by this entry on the next line with same indentation.

##### Local settings:
Add file called "config.local.json" to config/ directory of project root directory
In addition to existing "config.json" settings, this file is used to store private configuration settings like passwords

##### How to run:
Runnable modules:

- load_neighbors.py
- test/unit_tests_load_neighbors.py

LOAD_NEIGHBORS:

```
	python load_neighbors.py
```

UNIT_TESTS:

```
    python test/unit_tests_load_neighbors.py 
```

To get information about any runnable module:

* python <moduleName.py> -h
* python <moduleName.py> --help

This will tell you how to run the program along with its available command line parameters.