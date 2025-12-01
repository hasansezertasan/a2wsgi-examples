"""Tests for the application."""

from __future__ import annotations

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root() -> None:
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello World"}


def test_starlette() -> None:
    """Test the starlette endpoint."""
    response = client.get("/starlette")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello Starlette"}


def test_fastapi() -> None:
    """Test the fastapi endpoint."""
    response = client.get("/fastapi")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello FastAPI"}


def test_flask() -> None:
    """Test the flask endpoint."""
    response = client.get("/flask")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello Flask"}


def test_bottle() -> None:
    """Test the bottle endpoint."""
    response = client.get("/bottle")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello bottle"}


def test_django() -> None:
    """Test the django endpoint."""
    response = client.get("/django")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello django"}


def test_blacksheep() -> None:
    """Test the blacksheep endpoint."""
    response = client.get("/blacksheep")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello blacksheep"}


def test_quart() -> None:
    """Test the quart endpoint."""
    response = client.get("/quart")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello quart"}


def test_falcon() -> None:
    """Test the falcon endpoint."""
    response = client.get("/falcon")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello falcon"}


def test_sanic() -> None:
    """Test the sanic endpoint."""
    response = client.get("/sanic")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello sanic"}


def test_pyramid() -> None:
    """Test the pyramid endpoint."""
    response = client.get("/pyramid")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello pyramid"}


def test_hug() -> None:
    """Test the hug endpoint."""
    response = client.get("/hug")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello hug"}


def test_robyn() -> None:
    """Test the robyn endpoint."""
    response = client.get("/robyn")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello robyn"}


def test_webapp2() -> None:
    """Test the webapp2 endpoint."""
    response = client.get("/webapp2")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello webapp2"}


def test_connexion() -> None:
    """Test the connexion endpoint."""
    response = client.get("/connexion")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello connexion"}


def test_tornado() -> None:
    """Test the tornado endpoint."""
    response = client.get("/tornado")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello tornado"}


def test_aiohttp() -> None:
    """Test the aiohttp endpoint."""
    response = client.get("/aiohttp")
    assert response.status_code == status.HTTP_200_OK, response.text
    assert response.json() == {"message": "Hello aiohttp"}
