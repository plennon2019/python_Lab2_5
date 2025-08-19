import pytest
from fastapi.testclient import TestClient
from main import app, users

@pytest.fixture(autouse=True)
def clear_users():
    # Clear the global users list before and after each test
    users.clear()
    yield
    users.clear()

@pytest.fixture
def client():
    return TestClient(app)
