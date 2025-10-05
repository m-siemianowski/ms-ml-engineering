
# 04_mlops_pipeline

Objective:
- Airflow (or Prefect) DAG for ETL -> Train -> Validate -> Deploy
- MLflow for experiment tracking and model registry
- FastAPI for model serving

Structure:
- airflow/    # DAGs, plugins, Dockerfile (optional)
- mlflow/     # local mlflow storage
- api/        # FastAPI app exposing model inference
- docker/     # docker configs and helper scripts
