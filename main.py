from src.pipeline.Stage1_dataINg import DataIngestionPipeline
from src.pipeline.Stage2_data_tranformation import DataTransformationPipeline
from src.pipeline.Stage3_modelEval import ModelEvalutionPipeline

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
    Data_Transformation_Pipeline = DataTransformationPipeline()
    Data_Transformation_Pipeline.initateDataTransformation()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Evalution stage'

try:
    logger.info(f'Initiating {STAGE_NAME} intiated')
    Data_Evalution_Pipeline = ModelEvalutionPipeline()
    Data_Evalution_Pipeline.initateModelEvalution()
    logger.info(f'{STAGE_NAME} initiated')
except Exception as e:
    logger.exception(e)
    raise e