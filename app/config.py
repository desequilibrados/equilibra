"""Configurações centrais da API Equilibra.

O backend é executado integralmente em Python e persiste seus dados em SQLite.
As configurações variáveis ficam fora do código para que o mesmo projeto possa ser
executado no notebook, em QA ou futuramente em outro ambiente sem alterar os fontes.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB_PATH = BASE_DIR / "equilibra.db"

# O .env existe apenas no computador do desenvolvedor e nunca deve ser versionado.
load_dotenv(BASE_DIR / ".env")


def _csv_env(name: str, default: str) -> list[str]:
    """Transforma uma variável separada por vírgulas em uma lista limpa."""

    value = os.getenv(name, default)
    return [item.strip() for item in value.split(",") if item.strip()]


class Config:
    """Configuração padrão para desenvolvimento e demonstração local."""

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{DEFAULT_DB_PATH.as_posix()}",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    AUTO_CREATE_DB = os.getenv("AUTO_CREATE_DB", "true").lower() == "true"

    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "5000"))
    API_DEBUG = os.getenv("API_DEBUG", "false").lower() == "true"

    # Preparação mínima para o frontend web futuro. Em produção, não usar origem "*".
    CORS_ORIGINS = _csv_env(
        "CORS_ORIGINS",
        "http://localhost:3000,http://localhost:5173",
    )


class TestConfig(Config):
    """Configuração isolada usada pela suíte automatizada."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    AUTO_CREATE_DB = True
    CORS_ORIGINS = ["http://localhost:5173"]
