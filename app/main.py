from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.routes import health

app = FastAPI(title="Legal CI/CD App")

# Include existing health router
app.include_router(health.router)

# Resolve static directory safely (works inside Docker too)
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

# Mount static folder
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve frontend at root URL
@app.get("/")
def serve_frontend():
    return FileResponse(STATIC_DIR / "index.html")