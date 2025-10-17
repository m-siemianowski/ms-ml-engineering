
import joblib, pandas as pd, numpy as np, os
from src.utils import load_config, load_data
from src.features import build_features

def predict(latest_n=30):
    cfg = load_config('config.yaml')
    data_cfg = cfg['data']
    train_cfg = cfg['training']

    df = load_data(data_cfg['path'], date_col=data_cfg.get('date_col','date'))
    df_feat = build_features(df, {**cfg.get('features',{}), 'target_col': data_cfg.get('target_col','close')})

    model_path = train_cfg.get('model_path','models/xgb_model.joblib')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    model = joblib.load(model_path)

    # take last row(s) for prediction - here we use last available features row
    X = df_feat.tail(1).drop(columns=['date','close'], errors='ignore')
    pred = model.predict(X)[0]
    last_date = df_feat['date'].iloc[-1]
    return {'last_date': str(last_date.date()), 'horizon': train_cfg.get('target_horizon',5), 'prediction': float(pred)}

if __name__=='__main__':
    print(predict())
