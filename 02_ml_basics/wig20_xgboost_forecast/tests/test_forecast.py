import pytest
import pandas as pd
from pathlib import Path
from src.train_model import train_model
from src.predict import make_predictions
from src.utils import load_data
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
DATA_PATH = Path("data/wig20_daily.csv")

def test_data_loading():
    df = load_data(DATA_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert any(c.lower() == "close" for c in df.columns)

def test_model_training():
    df = load_data(DATA_PATH)
    model, X_test, y_test = train_model()
    assert model is not None
    assert len(X_test) == len(y_test)

def test_predictions():
    df = load_data(DATA_PATH)
    model, X_test, y_test = train_model()
    preds = make_predictions(model, X_test)
    assert len(preds) == len(y_test)
    assert all(isinstance(x, float) for x in preds)


