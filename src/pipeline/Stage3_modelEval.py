from src.config.configuration import ConfigurationManager
from src.components.modelevalution import ModelEvalution

class ModelEvalutionPipeline:
    def __init__(self):
        pass

    def initateModelEvalution(self):
        config = ConfigurationManager()
        get_modelEval= config.get_model_eval()
        modeleval = ModelEvalution(config=get_modelEval)
        modeleval.predict()