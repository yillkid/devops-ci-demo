"""hello —— DevOps 課的範例 FastAPI app。

一路用到：pytest（單元測試）、GitHub Actions（CI）、Docker、K8S、ArgoCD。
"""
from fastapi import FastAPI

from app.login import router as login_router

VERSION = "v1.0"

app = FastAPI(title="hello")
app.include_router(login_router)


@app.get("/")
def root():
    # version 字串之後做 blue-green / canary、確認新版上線時會用到
    return {"service": "hello", "version": VERSION}


@app.get("/health")
def health():
    # 給 K8S liveness/readiness、Docker healthcheck 用
    return {"status": "ok"}
