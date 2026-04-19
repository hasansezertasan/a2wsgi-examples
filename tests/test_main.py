"""Tests for the application."""

from __future__ import annotations

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client() -> TestClient:
    """Create a test client for the application."""
    return TestClient(app)


# --- Sub-application index endpoints ---


@pytest.mark.parametrize(
    ("path", "expected_message"),
    [
        ("/", "Hello World"),
        ("/starlette", "Hello starlette"),
        ("/fastapi", "Hello fastapi"),
        ("/flask", "Hello flask"),
        ("/bottle", "Hello bottle"),
        ("/django", "Hello django"),
        ("/blacksheep", "Hello blacksheep"),
        ("/quart", "Hello quart"),
        ("/falcon", "Hello falcon"),
        ("/sanic", "Hello sanic"),
        ("/pyramid", "Hello pyramid"),
        ("/hug", "Hello hug"),
        ("/robyn", "Hello robyn"),
        ("/webapp2", "Hello webapp2"),
        ("/connexion", "Hello connexion"),
        ("/tornado", "Hello tornado"),
        ("/aiohttp", "Hello aiohttp"),
        ("/litestar", "Hello litestar"),
    ],
)
def test_sub_app_index(client: TestClient, path: str, expected_message: str) -> None:
    """Test each sub-application returns its greeting."""
    response = client.get(path)
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": expected_message}


# --- Redirect endpoint ---


def test_application_redirection(client: TestClient) -> None:
    """Test the application redirection endpoint."""
    response = client.get("/application-redirection/flask", follow_redirects=False)
    assert response.status_code == status.HTTP_302_FOUND
    assert response.headers["location"] == "/flask"


def test_application_redirection_invalid(client: TestClient) -> None:
    """Test redirect with invalid application name returns 422."""
    response = client.get("/application-redirection/nonexistent")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


# --- FastAPI sub-app cookie endpoints ---


def test_fastapi_set_cookie(client: TestClient) -> None:
    """Test setting a cookie via FastAPI sub-app."""
    response = client.post("/fastapi/cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Cookie set"}
    assert "application" in response.cookies
    assert response.cookies["application"] == "fastapi"


def test_fastapi_get_cookie(client: TestClient) -> None:
    """Test reading a cookie via FastAPI sub-app."""
    client.cookies.set("application", "fastapi")
    response = client.get("/fastapi/cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "fastapi"}
    client.cookies.clear()


def test_fastapi_get_cookie_missing(client: TestClient) -> None:
    """Test reading a missing cookie returns null."""
    client.cookies.clear()
    response = client.get("/fastapi/cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": None}


def test_fastapi_delete_cookie(client: TestClient) -> None:
    """Test deleting a cookie via FastAPI sub-app."""
    client.cookies.set("application", "fastapi")
    response = client.delete("/fastapi/cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Cookie deleted"}
    client.cookies.clear()


# --- Flask sub-app cookie endpoints ---


def test_flask_set_cookie(client: TestClient) -> None:
    """Test setting a cookie via Flask sub-app."""
    response = client.post("/flask/cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Cookie set"}
    assert "application" in response.cookies
    assert response.cookies["application"] == "flask"


def test_flask_get_cookie(client: TestClient) -> None:
    """Test reading a cookie via Flask sub-app."""
    client.cookies.set("application", "flask")
    response = client.get("/flask/cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "flask"}
    client.cookies.clear()


def test_flask_delete_cookie(client: TestClient) -> None:
    """Test deleting a cookie via Flask sub-app."""
    client.cookies.set("application", "flask")
    response = client.get("/flask/delete-cookie")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Cookie deleted"}
    client.cookies.clear()


def test_flask_get_cookies(client: TestClient) -> None:
    """Test listing all cookies via Flask sub-app."""
    response = client.get("/flask/cookies")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["message"] == "cookies"
    assert "cookies" in data


# --- Error paths ---


def test_nonexistent_path(client: TestClient) -> None:
    """Test 404 on unknown path."""
    response = client.get("/nonexistent")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_wrong_method_on_root(client: TestClient) -> None:
    """Test POST on root returns 405."""
    response = client.post("/")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
