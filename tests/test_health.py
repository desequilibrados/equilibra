"""Testes dos endpoints de identificação e status."""


def test_root_identifies_backend_and_database(client):
    response = client.get("/api/v1/")

    assert response.status_code == 200
    data = response.get_json()["data"]
    assert data["name"] == "Equilibra API"
    assert data["backend"] == "Python"
    assert data["database"] == "SQLite"


def test_health_endpoint_checks_database(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.get_json()["data"] == {
        "status": "healthy",
        "database": "connected",
    }
