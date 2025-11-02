# 08_databricks_mlops — Databricks and Scalable ML Pipelines

This module focuses on developing and deploying machine learning workflows in **Databricks** — a unified data and AI platform that combines **Apache Spark**, **Delta Lake**, and **MLflow**.  
It bridges the gap between local ML development and large-scale, production-grade model pipelines.

---

## 🎯 Objectives

- Build and manage data processing and ML pipelines using Databricks and Spark.  
- Track experiments and model performance using **MLflow**.  
- Leverage **Delta Lake** for reliable, versioned data storage.  
- Automate pipelines with **Jobs** and integrate CI/CD principles for MLOps.  

---

## 📁 Structure

08_databricks_mlops/  
├── data/ → Example datasets or Delta tables used for experiments  
├── jobs/ → Job definitions and scripts for Databricks automation  
├── mlflow_experiments/ → MLflow tracking and model registry experiments  
└── notebooks/ → Databricks notebooks for data processing and training  

---

## ⚙️ Getting Started

**Local setup (optional)**  
To run Databricks-related code locally, you can simulate parts of the environment using PySpark and MLflow:

1. Create and activate a virtual environment  
   python -m venv .venv  
   source .venv/bin/activate  

2. Install dependencies  
   pip install pyspark mlflow delta-spark  

**Databricks setup**  
1. Create a free Databricks Community Edition account → https://community.cloud.databricks.com  
2. Upload your notebooks from `/notebooks` to your workspace.  
3. Create or attach a compute cluster (recommended: Single Node, DBR 14+).  
4. Upload sample datasets from `/data` to DBFS or Delta tables.  
5. Configure MLflow tracking and start your first experiment.  

---

## 🚀 Planned Projects

| Project | Description |
|----------|-------------|
| 01_spark_data_preprocessing | Data processing and feature engineering in Spark |
| 02_mlflow_experiment_tracking | ML lifecycle management with MLflow |
| 03_delta_training_pipeline | Model training on Delta Lake tables |
| 04_job_automation | Schedule and orchestrate pipelines with Databricks Jobs |
| 05_end_to_end_mlops | Full production pipeline from data → model → registry |

---

## 🧩 Next Steps

- Integrate Databricks Repos for Git-based notebook sync.  
- Add MLflow model versioning and automatic deployment.  
- Experiment with Databricks AutoML for baseline model comparison.  
- Add CI/CD workflow using GitHub Actions or Databricks CLI.  

---

