
# 02_ml_basics - WIG20 Forecasting (Classic ML)

Objective:
- Feature engineering for time-series (lags, rolling windows)
- Train classical models: LinearRegression, RandomForest, XGBoost
- Produce reproducible training script and evaluation notebook

Run:
```bash
python src/train.py --config config/train.yaml
python src/predict.py --model-path models/best.pkl
```

Files to implement:
- src/data.py
- src/features.py
- src/train.py
- notebooks/analysis.ipynb
