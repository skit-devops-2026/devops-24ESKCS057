# Project Overview

ShopEase is a simple e‑commerce Flask application used as a pedagogical DevOps project. It demonstrates a typical CI/CD pipeline, containerisation, and prepares the ground for Kubernetes and monitoring extensions.

**Key features**
- Home page (`/`) with a welcome message.
- Health endpoint (`/health`) returning `{ "status": "healthy" }`.
- Product catalogue (`/products`), shopping cart (`/cart`), order list (`/orders`), and a basic search endpoint (`/search`).
- Dockerised for easy deployment (see `Dockerfile`).
- CI pipeline in GitHub Actions that runs hygiene checks, unit tests, and builds/pushes a container image.

The repository contains the following logical sections:
- `app.py` – application source.
- `requirements.txt` – Python dependencies.
- `test_app.py` – pytest suite.
- `Dockerfile` & `docker-compose.yml` – container definitions.
- `Jenkinsfile` – optional Jenkins pipeline.
- `k8s/` – Kubernetes manifests (deployment and service) for local testing (Phase 2).
- `monitoring/` – placeholder for Prometheus/Grafana setup (Phase 3).
- `docs/` – this documentation folder.

> **Note**: The official milestone checklist has not been provided. The table in `docs/tracker.md` is a provisional checklist that will be aligned with the official rubric once it becomes available.

## Kubernetes configuration

The repository now includes Kubernetes manifests (`deployment.yaml` and `service.yaml`) under the `k8s/` directory. These manifests have been created and can be applied to a local Kubernetes cluster (e.g., Minikube, kind, Docker Desktop). They have **not** been deployed or runtime‑tested yet; follow the instructions in `k8s/README.md` to try them locally.
