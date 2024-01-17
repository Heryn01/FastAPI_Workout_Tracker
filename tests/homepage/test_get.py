from fastapi.testclient import TestClient

from workout_tracker.main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json()[0]["first_name"]
