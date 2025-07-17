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
        "name": "Mary",
        "email": "mary@example.com",
        "age": 22
    }
    response = client.post("/api/users", json=user)
    assert response.status_code == 201
    assert response.json()["name"] == "Mary"
