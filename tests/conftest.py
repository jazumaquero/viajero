from fastapi.testclient import TestClient
from pytest import fixture
from app.awsgi import app


@fixture
def client():
    client = TestClient(app)
    return client
