from Extracter.youtube import YtCommentExtracter 
import os
from src.logging import logger
from src.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        self.config= config

    def youtubeComment(self,url):
        obj = YtCommentExtracter()
        ytcomm = obj.get_youtube_comments(url)
        logger.debug('yt Comment Text fetch successfully')
        with open(self.config.data_yt_path, "w", encoding="utf-8") as f:
            for comment in ytcomm:
                f.write(comment + "\n")
            logger.debug('yt Comment Text successfully saved in file')