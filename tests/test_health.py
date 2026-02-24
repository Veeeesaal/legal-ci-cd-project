import sys
import os

# Project root ko Python path me add karo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    
    assert response.status_code == 200
    
    data = response.json()
    
    # Check required fields
    assert data["status"] == "healthy"
    assert "message" in data