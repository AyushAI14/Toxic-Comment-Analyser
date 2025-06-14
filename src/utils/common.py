import os
import yaml
from src.logging import logger
from box import Box

def read_yaml_file(filepath:str)->Box:
    """
    This will read file related to yaml
    """
    try:
        with open(filepath,'w') as f:
            content = yaml.load(f)
        logger.debug(f"{filepath} has successfully been extracted")
        return Box(content)
    except Exception as e:
        raise e 

def create_dir(dirlist:list):
    
    try:
        for dir in dirlist:
            os.makedirs(dir,exist_ok=True)
    except Exception as e:
        raise e
