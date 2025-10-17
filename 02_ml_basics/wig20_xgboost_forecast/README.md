
# WIG20 XGBoost Forecast (02_ml_basics/wig20_xgboost_forecast)

This is a starter end-to-end project demonstrating feature engineering and XGBoost regression for short-horizon forecasting on a sample WIG20 dataset.

## Quickstart (local)

1. Create virtualenv and install requirements:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. Train model:
```bash
cd 02_ml_basics/wig20_xgboost_forecast
python src/train_model.py
```

3. Make a quick prediction:
```bash
python src/predict.py
```

## Structure
- data/: sample CSV data
- notebooks/: EDA & quick experiments
- src/: modular python code (features, train, predict)
- config.yaml: parameters and model path

## Notes
- The sample CSV is *synthetic* and only for demo. Replace `data/wig20.csv` with real data for better results.
- Next steps: hyperparameter tuning, cross-validation (TimeSeriesSplit), backtesting and API serving.
