
# 03_deep_learning - LSTM & Transformer Forecasting

Objective:
- Implement LSTM and Transformer architectures in PyTorch
- Compare to baseline classical models
- Expose model through FastAPI and Docker

Run (dev):
```bash
python src/train.py --config config/train_dl.yaml
docker build -t ms-ml-dl-api ./api
```
