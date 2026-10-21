## System Architecture

```mermaid
flowchart TD
    subgraph dev[Development]
        A[app.py] --> B[requirements.txt]
        B --> C[Dockerfile]
    end
    subgraph ci[CI]
        D[GitHub Actions] --> E[Run tests]
        E --> F[Build Docker image]
        F --> G[Push to GHCR]
    end
    subgraph cd[CD]
        H[Render deployment] --> I[Live URL]
    end
    subgraph k8s[Optional Kubernetes deployment]
        J[Deploy to local K8s cluster] --> K[Pod running Flask]
        K --> L[Service (ClusterIP)]
    end
    A --> D
    F --> H
    F --> J
```

The diagram shows the flow from source code through CI pipelines to the deployed Render application (existing) and an optional Kubernetes deployment path that can be used for local testing or future production.
