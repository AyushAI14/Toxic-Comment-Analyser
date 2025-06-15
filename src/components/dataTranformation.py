from src.logging import logger
from text_prettifier import TextPrettifier
from langdetect import detect
from src.entity import DataTranformationConfig


class DataTranformation:
    def __init__(self,config=DataTranformationConfig):
        self.config= config
        self.prettifier = TextPrettifier()

        with open(self.config.data_yt_path, "r", encoding="utf-8") as f:
                self.text = [line.strip() for line in f.readlines()]
                logger.info("yt Comment Text successfully loaded")

    def text_cleaner(self,text):
        text = text.lower()
        text = self.prettifier.remove_contractions(text)
        text = self.prettifier.remove_emojis(text)
        text = self.prettifier.remove_html_tags(text)
        text = self.prettifier.remove_urls(text)
        text = self.prettifier.remove_special_chars(text)
        text = self.prettifier.remove_stopwords(text)
        text = self.prettifier.remove_numbers(text)
        return text
    def is_english(self,text):
        try:
            return detect(text) == 'en'
        except:
            return False
        
    def filter_text(self):
        cleaned_text = [self.text_cleaner(t) for t in self.text]
        english_comments = [text for text in cleaned_text if self.is_english(text)]
        with open(self.config.clean_data_yt_path, "w", encoding="utf-8") as f:
            for comment in english_comments:
                f.write(comment + "\n")
            logger.debug('yt Comment Text successfully saved in file')
