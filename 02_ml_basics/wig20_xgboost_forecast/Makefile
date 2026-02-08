.PHONY: help install test train predict clean

help:
	@echo "Available commands:"
	@echo "  make install    - install dependencies"
	@echo "  make test       - run unit tests"
	@echo "  make train      - train model"
	@echo "  make predict    - run prediction"
	@echo "  make clean      - remove artifacts"

# Install dependencies
install:
	@echo "Installing dependencies..."
	python3 -m pip install --upgrade pip
	python3 -m pip install -r requirements.txt

# Run tests
test:
	@echo "Running tests..."
	python3 -m pytest -q --disable-warnings

# Train model
train:
	@echo "Training model..."
	python3 -m src.train_model

# Make predictions
predict:
	@echo "Making predictions..."
	python3 -c "from src.predict import make_predictions; print(make_predictions())"

# Clean artifacts
clean:
	@echo "Cleaning artifacts..."
	rm -rf .pytest_cache
	rm -rf models/*.joblib
