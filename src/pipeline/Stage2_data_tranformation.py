from src.config.configuration import ConfigurationManager
from src.components.dataTranformation import DataTranformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initateDataTransformation(self):
        config = ConfigurationManager()
        get_datatranConfig= config.get_data_transformation()
        dataTranformation = DataTranformation(config=get_datatranConfig)
        dataTranformation.filter_text()