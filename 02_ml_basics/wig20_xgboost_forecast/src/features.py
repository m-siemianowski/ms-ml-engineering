
import pandas as pd
import numpy as np

def create_lag_features(df, col='close', lags=[1,2,3]):
    for l in lags:
        df[f'lag_{l}'] = df[col].shift(l)
    return df

def create_rolling_features(df, col='close', windows=[3,7]):
    for w in windows:
        df[f'roll_mean_{w}'] = df[col].rolling(window=w).mean()
        df[f'roll_std_{w}'] = df[col].rolling(window=w).std()
    return df

def create_diff(df, col='close'):
    df['diff_1'] = df[col].diff(1)
    return df

def build_features(df, config):
    df = df.copy()
    df = create_lag_features(df, col=config.get('target_col','close'), lags=config.get('lags',[1,2,3]))
    df = create_rolling_features(df, col=config.get('target_col','close'), windows=config.get('rolling_windows',[3,7]))
    if config.get('diff', True):
        df = create_diff(df, col=config.get('target_col','close'))
    # drop rows with NA due to shifts/rolling
    df = df.dropna().reset_index(drop=True)
    return df
