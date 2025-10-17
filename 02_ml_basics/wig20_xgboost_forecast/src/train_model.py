
import os, joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import xgboost as xgb
from src.utils import load_config, load_data
from src.features import build_features

def prepare_targets(df, target_col='close', horizon=5):
    df = df.copy()
    df['target'] = df[target_col].shift(-horizon)
    df = df.dropna().reset_index(drop=True)
    return df

def train():
    cfg = load_config('config.yaml')
    data_cfg = cfg['data']
    train_cfg = cfg['training']

    df = load_data(data_cfg['path'], date_col=data_cfg.get('date_col','date'))
    df = build_features(df, {**cfg.get('features',{}), 'target_col': data_cfg.get('target_col','close')})

    df = prepare_targets(df, target_col=data_cfg.get('target_col','close'), horizon=train_cfg.get('target_horizon',5))

    feature_cols = [c for c in df.columns if c not in ['date','target','close']]
    X = df[feature_cols]
    y = df['target']

    # time-aware split
    split_idx = int(len(df)*(1-train_cfg.get('test_size',0.2)))
    X_train, X_test = X.iloc[:split_idx], X.iloc[split_idx:]
    y_train, y_test = y.iloc[:split_idx], y.iloc[split_idx:]

    model = xgb.XGBRegressor(**train_cfg.get('xgb_params', {}))
    model.fit(X_train, y_train,
              eval_set=[(X_train, y_train), (X_test, y_test)],
              early_stopping_rounds=20,
              verbose=False)

    preds = model.predict(X_test)
    rmse = mean_squared_error(y_test, preds, squared=False)
    print(f"Test RMSE: {rmse:.4f}")

    os.makedirs(os.path.dirname(train_cfg.get('model_path','models/xgb_model.joblib')), exist_ok=True)
    joblib.dump(model, train_cfg.get('model_path','models/xgb_model.joblib'))
    print('Model saved to', train_cfg.get('model_path','models/xgb_model.joblib'))

if __name__=='__main__':
    train()
