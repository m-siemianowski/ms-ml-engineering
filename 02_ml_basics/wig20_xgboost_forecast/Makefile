![CI](https://github.com/m-siemianowski/ms-ml-engineering/actions/workflows/ci.yml/badge.svg)

.PHONY: help venv install test train predict clean

VENV ?= .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

help:
	@echo "Available commands:"
	@echo "  make venv       - create virtual environment"
	@echo "  make install    - install dependencies"
	@echo "  make test       - run unit tests"
	@echo "  make train      - train model"
	@echo "  make predict    - run prediction"
	@echo "  make clean      - remove artifacts"

venv:
	python3 -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

test:
	$(PYTHON) -m pytest -q --disable-warnings

train:
	$(PYTHON) -m src.train_model

predict:
	$(PYTHON) -c "from src.predict import make_predictions; print(make_predictions())"

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf models/*.joblib
	rm -rf __pycache__
