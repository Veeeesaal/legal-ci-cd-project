from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="Legal CI/CD App")

app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "CI/CD Deployment Successful"}
