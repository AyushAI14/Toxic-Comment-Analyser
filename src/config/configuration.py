from src.constants import *
from src.utils.common import read_yaml_file,create_dir
from src.entity import DataIngestionConfig,DataTranformationConfig,ModelEvalutionConfig

class ConfigurationManager:
    def __init__(self,config=CONFIG_FILE_PATH,
                 param=PARAM_FILE_PATH):
        self.config=read_yaml_file(config)
        self.param=read_yaml_file(param)
        create_dir([self.config.artifact_root])

    def get_data_ingestion(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_dir([config.root_dir])
        get_dataINgestion=DataIngestionConfig(
            root_dir=config.root_dir,
            data_yt_path=config.data_yt_path,
            data_tw_path=config.data_tw_path,
            data_nor_path=config.data_nor_path
        )
        return get_dataINgestion

    def get_data_transformation(self)->DataTranformationConfig:
        config = self.config.data_transformation
        create_dir([config.root_dir])
        get_dataTran=DataTranformationConfig(
            root_dir=config.root_dir,
            clean_data_yt_path=config.clean_data_yt_path,
            data_yt_path=config.data_yt_path
        )
        return get_dataTran

    def get_model_eval(self)->ModelEvalutionConfig:
        config = self.config.model_evalution
        create_dir([config.root_dir])
        get_modelEval=ModelEvalutionConfig(
            root_dir=config.root_dir,
            clean_data_yt_path=config.clean_data_yt_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path

        )
        return get_modelEval