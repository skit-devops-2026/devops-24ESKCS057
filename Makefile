.PHONY: install test build run docker-build docker-up

install:
	pip install -r requirements.txt

test:
	python -m pytest

build:
	@echo "No build step required for Python Flask application"

run:
	python app.py

docker-build:
	docker build -t shopease .

docker-up:
	docker compose up --build