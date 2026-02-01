.PHONY: help venv install test train predict clean

help:
	@echo "Available commands:"
	@echo "  make venv       - create virtual environment"
	@echo "  make install    - install dependencies"
	@echo "  make test       - run unit tests"
	@echo "  make train      - train model"
	@echo "  make predict    - run prediction"
	@echo "  make clean      - remove artifacts"

venv:
	python3 -m venv .venv

install:
	pip install --upgrade pip
	pip install -r requirements_37.txt

test:
	pytest -q --disable-warnings

train:
	python -m src.train_model

predict:
	python -c "from src.predict import make_predictions; print(make_predictions())"

clean:
	rm -rf .pytest_cache
	rm -rf models/*.joblib

