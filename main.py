from src.pipeline.Stage1_dataINg import DataIngestionPipeline
from src.pipeline.Stage2_data_tranformation import DataTransformationPipeline
# from src.pipeline.stage4_model_eval import ModelEvalutionPipeline

from src.logging import logger

STAGE_NAME = 'Data ingestion stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Ingestion_Pipeline = DataIngestionPipeline()
    Data_Ingestion_Pipeline.initateDataINgestion('https://youtu.be/OLPwT05kYjw?si=vlkgvHWyquJVddHS')
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Ingestion_Pipeline = DataTransformationPipeline()
    Data_Ingestion_Pipeline.initateDataTransformation()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e
