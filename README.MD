# chestcancer_prediction_using_mlflow_dvc

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml (models parameters)
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
10. Update the dvc.yaml


```bash

# install requirements
$ pip install -r requirements.txt

```

## Dvc Commands

```
$ dvc init

$ dvc dag

$ dvc repro  #reproduce the results of a pipeline or a specific stage within a pipeline.


```