from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

app = FastAPI()
hits = Counter("hits", "Number of hits to the root")

@app.get("/")
def read_root():
    hits.inc()
    return {"message": "Hello new port from Kubernets, ArgoCD and add Grafana: hello-app:d2afd2c1d1fcb07d5ca22390714dd9ab043618ec"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

