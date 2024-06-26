from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

# Data Ingestion Stage
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX================X")
except Exception as e:
    logger.exception(e)

# Prepare Base Model Stage
STAGE_NAME = "Prepare base model"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX===============X")
except Exception as e:
    logger.exception(e)


STAGE_NAME ="Training"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX================X")
except Exception as e:
    logger.exception(e)
    
    
STAGE_NAME = "Evaluation Stage"

try:
    logger.info(f"*************************************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX===============X")
    
except Exception as e:
    logger.exception(e)
    raise e