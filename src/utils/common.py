import os
from pathlib import Path
import yaml
from src.logging import logger
from typing import Any
# from box import config_box
from box import Box  # fix import

def read_yaml_file(filepath: str) -> Box:  # optional typing update
    try:
        with open(filepath, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.debug("YAML file successfully loaded")
            return Box(content)  # call Box, not config_box
    except Exception as e:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


def create_dir(filepath_dirs: list):
    """
    Create directories from a list of paths.

    Args:
        filepath_dirs (list): List of directory paths to create.
    """
    for filepaths in filepath_dirs:
        os.makedirs(filepaths, exist_ok=True)
        logger.info(f"Created directory at: {filepaths}")
