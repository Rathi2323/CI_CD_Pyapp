import os
import sys

from app.main import app

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

def test_dummy():
    assert True
    
def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["message"] == "Hello DevOps!"
    
def test_health():
    client = app.test_client()
    response = client.get("/health")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["status"] == "UP"
       
def test_info():
    client = app.test_client()
    response = client.get("/info")
    json_data = response.get_json()
    assert "version" in json_data
    assert "commit" in json_data
    
def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")
    body = response.get_data(as_text=True)
    assert "app_uptime_seconds" in body