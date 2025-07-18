from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_users_initially_empty():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == []

def test_post_user():
    user = {
        "user_id": 1,
        "name": "Paul L",
        "email": "Paul@atu.ie",
        "age": 22
    }
    response = client.post("/api/users", json=user)
    assert response.status_code == 201
    assert response.json()["name"] == "Paul L"

def test_put_user():

    user = {
        "user_id": 1,
        "name": "Mary",
        "email": "mary@atu.ie",
        "age": 22
    }
    response = client.post("/api/users", json=user)

    user = {
        "user_id": 1,
        "name": "Tom",
        "email": "tom@atu.ie",
        "age": 52
    }
    response = client.put("/api/users/1", json=user)
    assert response.status_code == 200
    assert response.json()["name"] == "Tom"
