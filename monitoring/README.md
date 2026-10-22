# Monitoring Setup

This folder contains the Docker Compose configuration for a Prometheus and Grafana stack that scrapes the **ShopEase** Flask application.

## How to start
```bash
cd monitoring
docker compose up -d
```

- Prometheus will be available at `http://localhost:9090`.
- Grafana will be available at `http://localhost:3000` (default admin / password **admin**).
- The Grafana dashboard is provided in `dashboard.json`. Import it via **Create → Import** and select the JSON file.

## Prometheus configuration
`prometheus.yml` scrapes the Flask app at `host.docker.internal:5000` (the container network host). Ensure the Flask app is running on port 5000 on the host machine.

## Grafana dashboard
The dashboard visualises:
- Total request count per HTTP method and endpoint.
- 95th/99th percentile request latency.

Both panels query the Prometheus metrics exposed at `/metrics` by the Flask app.
