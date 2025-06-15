from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: str
    data_yt_path: str
    data_tw_path: str
    data_nor_path: str

@dataclass
class DataTranformationConfig:
    root_dir: str
    data_yt_path: str
    clean_data_yt_path: str

@dataclass
class ModelEvalutionConfig:
    root_dir: str
    clean_data_yt_path: str
    tokenizer_path:str
    model_path:str