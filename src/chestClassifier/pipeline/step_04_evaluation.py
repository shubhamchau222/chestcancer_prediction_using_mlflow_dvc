from chestClassifier.config.configuration import ConfigurationManager
from chestClassifier.components.model_evaluation_mlfow import Evaluation
from chestClassifier import logger
import dagshub


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow() ##logs the experiments and metrices to mlflow

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        logger.info(f">>>>>> Dags hub repository initializing <<<<<<")
        dagshub.init(repo_owner='shubhamair1996', repo_name='chestcancer_prediction_using_mlflow_dvc', mlflow=True)
        logger.info(f">>>>>> Dags hub repository initialized successfull <<<<<<")

        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            