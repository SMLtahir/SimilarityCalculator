# SimilarityCalculator

*Python open source package that computes similarities between a list of items based on their tag relevance scores 
and prints the top neighbors of each item to file.* 

#### Set **PYTHONPATH** environment variable to your Python bin directory

#### Set **SIMCALC_HOME** in config.local.json
In SimilarityCalculator/config/ directory, create file config.local.json and paste,

```
{

        "SIMCALC_HOME": "<DIRECTORY_WHERE_SimilarityCalculator_IS_LOCATED>"
}
```

If the file was already created and there are more entries, add a comma followed by this entry on the next line with same indentation.
