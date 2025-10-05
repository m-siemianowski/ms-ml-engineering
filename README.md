
# ms-ml-engineering

Portfolio repository skeleton for transition from Senior Data Developer → Machine Learning / AI Engineer.
Full Hybrid track: Forecasting (time series) + AI/NLP (HuggingFace).

This repo contains a structured set of project templates, deployment configs and MLOps scaffolding:
- Local Docker Compose demo for API + MLflow + (light) services
- Cloud deployment examples for AWS SageMaker and GCP Vertex AI (templates & instructions)
- Project templates: Python advanced, ML basics, Deep Learning forecasting, NLP, MLOps pipeline, Cloud examples
- CI config, pre-commit and basic GitHub Actions workflow template

## Quick start (local demo)
```bash
unzip ms-ml-engineering.zip -d .
cd ms-ml-engineering/04_mlops_pipeline/api
# build the API container (example)
docker build -t ms-ml-api .
# or run docker-compose in the project root to spin up api + mlflow (if docker is installed)
docker-compose up --build
```

See each project folder for per-project run instructions.

Contact: your.name@example.com
