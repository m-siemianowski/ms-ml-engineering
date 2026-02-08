# WIG20 XGBoost Forecast (02_ml_basics/wig20_xgboost_forecast)

Starter end-to-end project demonstrating feature engineering and XGBoost regression
for short-horizon time-series forecasting on a sample WIG20 dataset.

The project is structured to be reproducible, testable, and CI-ready using a Makefile
as a single entry point for local development and GitHub Actions.

## Requirements

- Python 3.11
- make

## Quickstart (local & CI-compatible)

1. Create virtual environment and install dependencies:
    - `make install`

2. Run unit tests:
    - `make test`

3. Train the model:
    - `make train`

4. Run a quick prediction:
    - `make predict`

## Project structure

- `data/` – sample CSV data
- `notebooks/` – EDA and quick experiments
- `src/` – modular Python code (features, training, prediction)
- `tests/` – pytest-based unit tests
- `models/` – trained model artifacts
- `config.yaml` – model and feature configuration
- `Makefile` – single entry point for local runs and CI

## Notes

- The sample CSV data is *synthetic* and intended for demonstration only. Replace it with real WIG20 data for meaningful results.
- Current implementation focuses on a minimal, testable baseline.
- Next logical steps:
    - time-series cross-validation (`TimeSeriesSplit`)
    - hyperparameter tuning
    - backtesting
    - model versioning and artifact storage
    - API serving (FastAPI)

