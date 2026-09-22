"""Fixtures compartilhadas da suíte de testes."""

import pytest

from app import create_app
from app.config import TestConfig
from app.extensions import db


@pytest.fixture()
def app():
    """Cria uma aplicação com SQLite em memória para cada teste."""

    test_app = create_app(TestConfig)
    with test_app.app_context():
        db.create_all()
        yield test_app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """Cliente HTTP de teste do Flask."""

    return app.test_client()


@pytest.fixture()
def valid_user_payload():
    """Payload válido reutilizado pelos testes de integração."""

    return {
        "name": "Usuário Teste",
        "age": 30,
        "weight_kg": 78.5,
        "height_cm": 175,
        "activity_level": "moderado",
        "goal": "manter_peso",
        "preferences": ["frutas", "arroz"],
        "restrictions": [],
    }
