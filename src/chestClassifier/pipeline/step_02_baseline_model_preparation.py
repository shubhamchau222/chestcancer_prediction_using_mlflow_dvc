from chestClassifier.config.configuration import ConfigurationManager
from chestClassifier.components.prepare_basemodel import PrepareBaseModel
from chestClassifier import logger


STAGE_NAME= "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        base_model_config= config.get_prepare_base_model_config()
        prepare_base_model= PrepareBaseModel(config=base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e