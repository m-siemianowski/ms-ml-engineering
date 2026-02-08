# ms-ml-engineering

A structured portfolio repository showcasing **Machine Learning, Deep Learning, MLOps, and Cloud deployment workflows**.
Includes project templates, deployment scaffolding, and demonstration pipelines for both **time series forecasting** and **NLP (HuggingFace)** applications.

## Features

* **Local Docker Compose demo** for API + MLflow + supporting services
* **Cloud deployment templates** for AWS SageMaker and GCP Vertex AI
* **Project templates** including:

  * Advanced Python development
  * Machine Learning fundamentals
  * Deep Learning forecasting
  * Natural Language Processing
  * MLOps pipeline examples
  * Cloud deployment demonstrations
* **CI/CD scaffolding**: pre-commit hooks and GitHub Actions templates

## Quick Start (Local Demo)

```bash
unzip ms-ml-engineering.zip -d .
cd ms-ml-engineering/04_mlops_pipeline/api

# Build the API container
docker build -t ms-ml-api .

# Or run docker-compose from the project root to start API + MLflow
docker-compose up --build
```

For detailed instructions, see the README in each project folder.

## Contact

For questions or feedback, contact: [your.name@example.com](mailto:your.name@example.com)
