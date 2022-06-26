#any helper functions are written in the util file
#
#like reading the yaml file or how to create and read a pickle file 
#this function is not part of the pipeline

import yaml
from housing.exception import housing_exception
import os,sys

def read_yaml_file(filepath:str)->dict:
    """
    reads YAML file and returns the contents as a dictionary.
    """
    try:
        with open(config_file_path,"rb") as f:
            return yaml.safe_load(f)
            
    
    except Exception as e:
        raise housing_exception(e,sys) from e