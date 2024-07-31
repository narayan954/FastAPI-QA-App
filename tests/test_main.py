# tests/test_main.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users/", json={"username": "testuser"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_get_user_score():
    response = client.get("/users/1/score")
    assert response.status_code == 404  # Assuming no user yet


def test_update_user_credits():
    response = client.post("/users/1/credits", json={"user_id": 1, "credits": 100})
    assert response.status_code == 200
    assert response.json()["credits"] == 100
