# function to read the yaml file
import os
import pandas as pd
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path): # we have specified the filepath in path.config
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in the given path")
        
        with open(file_path,'r') as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Succesfully read the yamal file")
            return config # where all content of yaml file is stored
        
    except Exception as e:
        logger.error("ERROR while reading YAML file")
        raise CustomException("Failed to read yaml file", e)
    
def load_data(path):
    try:
        logger.info("Loading Data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}") 
        raise CustomException("Failed to load data")