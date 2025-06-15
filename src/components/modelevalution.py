from collections import Counter
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
from src.logging import logger
from src.entity import ModelEvalutionConfig

class ModelEvalution:
    def __init__(self,config=ModelEvalutionConfig):
        self.config=config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.config.model_path)
        self.pipeline =  TextClassificationPipeline(model=self.model, tokenizer=self.tokenizer)

        with open(self.config.clean_data_yt_path, "r", encoding="utf-8") as f:
                self.text = [line.strip() for line in f.readlines()]
                logger.info("yt Comment Text successfully loaded")
        
    def predict(self):
        result = [self.pipeline(c) for c in self.text]
        flat_preds = [x[0] for x in result]
        labels = [entry['label'] for entry in flat_preds]
        scores = [entry['score'] for entry in flat_preds]
        most_common_label = Counter(labels).most_common(1)[0][0]
        most_common_label_count = Counter(labels).most_common(1)[0][1]
        percentage = (most_common_label_count/len(labels))*100
        print(f"Result = Your comments are {percentage:.1f}% {most_common_label} with an average model confidence of {np.mean(scores):.2f}.")
            