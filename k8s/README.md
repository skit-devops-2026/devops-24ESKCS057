# Kubernetes Deployment Guide

This guide explains how to run the ShopEase Flask application on a local Kubernetes cluster (Minikube, Kind, or Docker Desktop).

## Prerequisites

- **Docker** installed and running.
- A local Kubernetes cluster reachable with `kubectl`. Examples:
  - **Minikube** (`minikube start`)
  - **Kind** (`kind create cluster`)
  - **Docker Desktop** with Kubernetes enabled.
- `kubectl` version 1.36+ (already present in the repository).

## 1. Build or pull the container image

The manifests use the image published to GitHub Container Registry:
```
ghcr.io/skit-devops-2026/devops-24eskcs057:latest
```
If the image is public you can apply the manifests directly.  If the registry requires authentication, create an image‑pull secret:
```powershell
# Replace <TOKEN> with a Personal Access Token that has read:packages scope
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=YOUR_GITHUB_USERNAME \
  --docker-password=<TOKEN> \
  --docker-email=you@example.com
```
Then edit `k8s/deployment.yaml` and add:
```yaml
      imagePullSecrets:
      - name: ghcr-secret
```
(Do **not** commit the secret file.)

If you prefer to use a locally built image:
```powershell
# Build the image locally (run from the repository root)
docker build -t shopease-local:latest .
# Load it into the cluster (example for Kind)
kind load docker-image shopease-local:latest
```
Modify `k8s/deployment.yaml` to use `shopease-local:latest` as the image.

## 2. Apply the manifests

```powershell
# From the repository root
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
You should see the resources created:
```powershell
kubectl get deployments pods services
```

## 3. Verify the Deployment

- **Pod status**: `kubectl get pods -l app=shopease`
- **Events** (if a pod fails): `kubectl describe pod <pod-name>`
- **Logs**: `kubectl logs <pod-name>`

## 4. Access the application

The Service is a `ClusterIP` exposing port 80 and routing to container port 5000.
To reach it from your workstation, use port‑forwarding:
```powershell
kubectl port-forward svc/shopease-service 8080:80
```
Then open a browser or curl:
```powershell
curl http://localhost:8080/
curl http://localhost:8080/health
```
You should receive the welcome message and a JSON health response.

## 5. Clean up

When finished, delete the resources:
```powershell
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
```
If you created a secret, delete it as well:
```powershell
kubectl delete secret ghcr-secret
```

---
**Note**: These manifests have been *statically* validated and can be applied to a local cluster. The repository does **not** contain a running Kubernetes deployment; you must execute the steps above to test it.
