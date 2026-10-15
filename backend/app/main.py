
from fastapi import FastAPI
from app.api.transactions import router as transactions_router

app = FastAPI(
    title="NEXORA Finance API",
    version="0.1.0",
    description="Financial management platform"
)


@app.get("/")
def home():
    return {
        "project": "NEXORA Finance",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(transactions_router)