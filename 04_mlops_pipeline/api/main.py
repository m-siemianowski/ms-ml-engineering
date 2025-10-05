
from fastapi import FastAPI
from pydantic import BaseModel
import joblib, os

app = FastAPI(title="ms-ml-engineering API")

MODEL_PATH = os.environ.get("MODEL_PATH", "/app/models/dummy_model.pkl")

class PredictRequest(BaseModel):
    features: list

@app.get('/health')
def health():
    return {"status": "ok"}

@app.post('/predict')
def predict(req: PredictRequest):
    # Dummy implementation - replace with real model loading & inference
    if not os.path.exists(MODEL_PATH):
        return {"error": "model not found", "model_path": MODEL_PATH}
    model = joblib.load(MODEL_PATH)
    X = [req.features]
    preds = model.predict(X)
    return {"predictions": preds.tolist()}
