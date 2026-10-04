# DevOps Python Application

A simple Python Flask application created for DevOps practice.

## Endpoints

GET /

GET /health

GET /api/users

GET /api/users/<id>

## Run locally

pip install -r requirements.txt

python app.py

## Docker

docker build -t devops-python-app:1.0 .

docker run -d --name devops-app -p 5000:5000 devops-python-app:1.0
