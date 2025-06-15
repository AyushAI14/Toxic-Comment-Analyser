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