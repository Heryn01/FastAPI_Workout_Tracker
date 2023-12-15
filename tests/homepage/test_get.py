from projectnamehere.app.main import app

from fastapi import FastAPI
from fastapi.testclient import TestClient

client = TestClient(app)

def test_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"Hello":"World"}