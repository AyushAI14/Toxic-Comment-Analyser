from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initateDataINgestion(self,url):
        config = ConfigurationManager()
        get_dataingestionConfig= config.get_data_ingestion()
        dataingestion = DataIngestion(config=get_dataingestionConfig)
        dataingestion.youtubeComment(url)