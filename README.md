# SimilarityCalculator

*Python open source package that computes similarities between a list of items based on their tag relevance scores 
and prints the top neighbors of each item to file.* 

##### Travis Continuous Integration Testing status 

[![Build Status](https://travis-ci.org/SMLtahir/SimilarityCalculator.svg?branch=master)](https://travis-ci.org/SMLtahir/SimilarityCalculator)

For maximum assurance against bugs, Travis CI testing is linked to the source Github repository. Travis runs several 
unit tests on the latest code pushed to Github and displays a badge indicating **Build_Passing** or 
**Build_Failing**. Since this project is currently under continuous development, it is suggested however to use only 
stable builds released as code versions.

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


##### Parallel execution

The SimilarityCalculator has been designed to run on maximum available CPUs and using several C implementations 
over native Python. Due to this, it is extremely fast and efficient. In case the user wants less CPUs to be used during 
similarity and nearest neighbor computation, the **NUMBER_OF_CPU** configurational parameter should be set appropriately.
Its default value is **MAX**.

##### Configuration Parameters

There are 3 json files in the SimilarityCalculator/config/ directory: 
1. **config.json** - This is the most general config file. Store parameters whose values you do not plan to change 
very often, here. These usually include input/output file paths, etc.
2. **config.test.json** - This file should be used for test parameters or parameters whose values you plan to change 
very frequently. This can include number of CPUs, neighborhood size, etc. 
3. **config.local.json** - This file is not written to the Github repository and will have to be created when 
the code is first used. This is used to store local and private parameters and their values. **DO NOT** store these 
parameters in any of the other config files.

In case the same configuration parameter is set in two or more files than the following is the order of assignment.
config.local.json > config.test.json > config.json
This means that if a parameter is set in both, local as well as test config files, then the value of the 
parameter in config.test will be overwritten by config.local and so on.  

The following parameters are to be modified as desired in these files.

1. **NUMBER_OF_CPU**

    *Example entry*:
    
        "NUMBER_OF_CPU": 2
    
    *Default entry*: 
    
        "NUMBER_OF_CPU": "MAX"
            
            
    This is used to indicate the number of CPUs to be used in parallel by the program. If not changed by the user, 
    the default is "MAX" which means that maximum available CPUs will be used for computation. Use this option for 
    large datasets and when speedy computation is required. An example of another value as it would appear in the 
    config file would be,
        
2. **FILE_RELEVANCE_PREDICTIONS**

    *Example entry*:
    
        "FILE_RELEVANCE_PREDICTIONS": "correct/path/inserted/here/sample_file.csv"
    
    *Default entry*: 
    
        "FILE_RELEVANCE_PREDICTIONS": "data/relevance_predictions.txt"

    This is the path to the main input file. It is suggested to store all data files in the SimilarityCalculator/data/ 
    directory. The input file can be a .txt, .csv (comma separated) or .tsv (tab separated) file. 
    It contains 3 values: 
    
        item1_id,item2_id,relevance_score
        
    Please reserve the first line of the file as the Header line for better readability.
    The comma (,) can be replaced by any **INPUT_FIELD_SEPARATOR** as long as it is declared in the 
    **INPUT_FIELD_SEPARATOR** configuration parameter (see below). 
    
    Item1 is an entity of a set on which you need to perform the nearest-neighbor analysis. Item2 (henceforth called 
    **tag**) is an entity that is used as a metric to compare two entities of the item1 set. 
    
    * Example 1:
     
         MovieId,Genre,RelevanceScore
         1,"Action",0.50
         1,"Comedy",0.75
         2,"Action",0.67
         2,"Comedy",0.30
         3,"Action",0.98
         3,"Comedy",0.10
    
    The example above can be used to check how similar two movies are based on how highly they can be classified to the 
    different genres. Normalization of scores is done within the program and so this should not be a worry at the time 
    of preparing the needed input file.
    
    * Example 2:
    
        UserId,MovieId,Rating
        1,96,4.5
        1,54,2.0
        2,96,5.0
        2,54,1.0
        3,96,3.0
        3,54,4.0
        
    The example above can be used to find how closely matched the tastes of different users are, on the basis of the 
    ratings they assign to movies.
    
    Fully working examples (input + output files) can be found in the SimilarityCalculator/data/samples/ directory.
    
    This code has been tested successfully on data files containing up to 2.5 million lines.    

3. **INPUT_FIELD_SEPARATOR**

    *Example entry* (tab-space):
    
        "INPUT_FIELD_SEPARATOR": "\t"
    
    *Default entry* (comma): 
    
        "INPUT_FIELD_SEPARATOR": ","
        
    This is the token (space, tab-space, comma, colon, semi-colon, etc.) that is used to separate two fields of the 
    input files. Examples can be seen above. 
    
4. **TAG_WEIGHTED**
    
    *Valid entries*:
    
        "TAG_WEIGHTED": "T"
        "TAG_WEIGHTED": "F"
    
    *Default entry*: 
    
        "TAG_WEIGHTED": "F"
    
    This configuration parameter can take only two values - "T" (True) and "F" (False). By default its value is F which 
    means that tags will be all equally weighted (= 1.0). Assign a value of "T" when some tags (as described above) need 
    to be weighted differently than others. This could happen if you want some tags to play a bigger role in determining 
    the nearest neighbors than others. 
        
5. **FILE_TAG_WEIGHTS**
 
    *Example entry*:
    
        "FILE_TAG_WEIGHTS": "correct/path/inserted/here/sample_tag_file.csv"
    
    *Default entry*: 
    
        "FILE_TAG_WEIGHTS": "data/tagWeights.txt"        

    This is an optional input file. The value of this parameter will be considered only when the parameter 
    **TAG_WEIGHTED** is set to "T" (True). The format of this file is as follows:
    
        tag,tag_weight
        
    Please reserve the first line of the file as the Header line for better readability.
    The comma (,) can be replaced by any **INPUT_FIELD_SEPARATOR** as long as it is declared in the 
    **INPUT_FIELD_SEPARATOR** configuration parameter (see above). The below is a tab-delimited example. 

    *Example*:
    
    tag weight
    "tagA"  2.3
    "tagB"  1.0
    "tagC"  -2.0
    
    **Please note**: If this file is included, **ALL** tags must be assigned weights.

6. **FILE_NEIGHBORS**

    *Example entry*:
    
        "FILE_NEIGHBORS": "correct/path/inserted/here/sample_file.txt"
    
    *Default entry*: 
    
        "FILE_NEIGHBORS": "data/neighbors.txt"
        
    This configuration parameter tells the program where to store the final output file. The format of the file produced
    will be as below:
    
        itemId,neighbor1,Similarity_Score
        
    *Example*:
    
        1       1       4.7657
        1       2       4.6790
        1       4       4.4423
        1       5       4.4208
        1       3       2.8345
        2       2       4.7657
        2       1       4.6790
        2       4       4.5840
        2       5       4.5061
        2       3       2.9758
    
    As can be seen in the example above, the neighbors of a particular itemId are printed in decreasing order of 
    similarity score. This means that the nearest neighbors will be displayed on top. 
    
7. **NEIGHBORHOOD_SIZE** 

    *Example entry*:
    
        "NEIGHBORHOOD_SIZE": 50
    
    *Default entry*: 
    
        "NEIGHBORHOOD_SIZE": 250
        
    This determines the number of top neighbors that you would want the program to calculate per item. If this value is 
    set higher than the total number of items, all items will be printed along with their similarity scores as 
    neighbors for every item.
    
    **More documentation has to be written below**
    
8. **LOG_NAME**

    *Example entry*:
    
        "LOG_NAME": "correct/path/inserted/here/sample_file.txt"
    
    *Default entry*: 
    
        "LOG_NAME": "logs/load_neighbors.txt"            
            
9. **ITEM1_COLUMN_NO**

    *Example entry*:
    
        "ITEM1_COLUMN_NO": "5"
    
    *Default entry*: 
    
        "ITEM1_COLUMN_NO": "1"
        
10. **ITEM2_COLUMN_NO**

    *Example entry*:
    
        "ITEM2_COLUMN_NO": "4"
    
    *Default entry*: 
    
        "ITEM2_COLUMN_NO": "2"
        
11. **RELEVANCE_SCORE_COLUMN_NO**

    *Example entry*:
    
        "RELEVANCE_SCORE_COLUMN_NO": "1"
    
    *Default entry*: 
    
        "RELEVANCE_SCORE_COLUMN_NO": "3"
        
**Similarity measures currently supported**
Currently, Similarity between items is calculated using the Cosine Similarity Measure. We are currently working to 
extend the code to include more measures. 
