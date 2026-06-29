"""Tests for the main application endpoints."""

from fastapi.testclient import TestClient
from main import app  # pylint: disable=import-error

client = TestClient(app)


def test_root():
    """Verify the root endpoint returns the expected greeting message"""
    response = client.get("/")
    assert response.status_code == 200
    assert {"message": "Hello World"} == response.json()


def test_status_endpoint():
    """Verify the status endpoint returns a healthy status response"""
    response = client.get("/status")
    assert response.status_code == 200
    assert {"status": "OK"} == response.json()


def test_post_not_allowed_on_root():
    """Verify that POST requests are rejected on the GET-only root endpoint"""
    response = client.post("/", json={"username": "dog", "password": "cats11"})
    assert response.status_code == 405
