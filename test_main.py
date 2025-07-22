from fastapi.testclient import TestClient
from main import app, users

client = TestClient(app)

test_user = {
    "user_id": 1,
    "name": "Mary",
    "email": "mary@atu.ie",
    "age": 22,
    "address": {
        "street": "Main Street",
        "number": 1,
        "county": "Galway",
        "country": "Ireland",
        "eircode": "H91F123"
    }
}
def setup_function():
    print("Clearing users, length before clear:", len(users))
    users.clear()

def test_get_users_initially_empty():
    response = client.get("/api/users")
    assert response.status_code == 200
    assert response.json() == []

def test_post_user():
    response = client.post("/api/users", json=test_user)
    assert response.status_code == 201
    assert response.json()["name"] == "Mary"

def test_put_user():
    user = {
        "user_id": 2,
        "name": "Tony",
        "email": "tony@atu.ie",
        "age": 22,
        "address": {
            "street": "Main Street",
            "number": 1,
            "county": "Galway",
            "country": "Ireland",
            "eircode": "H91F123"
        }
    }
    client.post("/api/users", json=test_user)
    client.post("/api/users", json=user)
    response = client.get("api/users")
    users = response.json()
    assert len(users) == 2

    user = {
        "user_id": 2,
        "name": "Tom",
        "email": "tom@atu.ie",
        "age": 52,
        "address": {
            "street": "Main Street",
            "number": 1,
            "county": "Galway",
            "country": "Ireland",
            "eircode": "H91F123"
        }
    }
    response = client.put("/api/users/2", json=user)
    assert response.status_code == 200
    assert response.json()["name"] == "Tom"

def test_get_user():
    response = client.post("/api/users", json=test_user)
    response = client.get("/api/user/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Mary"

def test_delete_user():

    user = {
        "user_id": 3,
        "name": "Mary",
        "email": "mary@atu.ie",
        "age": 22,
        "address": {
            "street": "Main Street",
            "number": 1,
            "county": "Galway",
            "country": "Ireland",
            "eircode": "H91F123"
        }
    }
    response = client.post("/api/users", json=user)
    assert response.json()["name"] == "Mary"

    response = client.delete("/api/users/3")
    assert response.status_code == 200
