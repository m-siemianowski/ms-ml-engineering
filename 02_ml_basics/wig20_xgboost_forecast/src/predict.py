import joblib, pandas as pd, os
from src.utils import load_config, load_data
from src.features import build_features

def make_predictions(model=None, X=None):
    """
    Generate predictions using the trained model.

    Args:
        model (xgb.XGBRegressor): Trained XGBoost model.
        X (pd.DataFrame, optional): Feature matrix for prediction.
            If None, uses the last available row from the dataset.

    Returns:
        preds (np.ndarray or float): Predicted values.
    """
    cfg = load_config('config.yaml')
    data_cfg = cfg['data']
    train_cfg = cfg['training']

    if model is None:
        model_path = train_cfg.get('model_path','models/xgb_model.joblib')
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")
        model = joblib.load(model_path)

    if X is None:
        df = load_data(data_cfg['path'], date_col=data_cfg.get('date_col','date'))
        df_feat = build_features(df, {**cfg.get('features',{}), 'target_col': data_cfg.get('target_col','close')})
        X = df_feat.tail(1).drop(columns=['date','close'], errors='ignore')

    return [float(x) for x in model.predict(X)]  # <-- force float conversion

if __name__=='__main__':
    preds = make_predictions()
    print(preds)
