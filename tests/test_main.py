from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_user():
    response = client.post("/users", json={"name": "Lucas", "email": "lucas@example.com", "age": 25})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Lucas"

def test_get_user_by_id():
    client.post("/users", json={"name": "Ana", "email": "ana@example.com", "age": 30})
    response = client.get("/users/2")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ana"

def test_update_user():
    client.post("/users", json={"name": "Carlos", "email": "carlos@example.com", "age": 40})
    response = client.put("/users/3", json={"name": "Carlos Silva", "email": "carlos.silva@example.com", "age": 41})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Carlos Silva"
    assert data["age"] == 41

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


