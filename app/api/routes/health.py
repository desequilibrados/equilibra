"""Rotas de identificação e saúde da API."""

from flask import Blueprint
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.api.responses import error, success
from app.extensions import db

health_bp = Blueprint("health", __name__)


@health_bp.get("/")
def root():
    """Retorna metadados simples para qualquer cliente identificar a API."""

    return success(
        {
            "name": "Equilibra API",
            "version": "1.0.0",
            "backend": "Python",
            "database": "SQLite",
            "status": "online",
        }
    )


@health_bp.get("/health")
def health():
    """Valida API e conexão com o banco usado no notebook/ambiente atual."""

    try:
        db.session.execute(text("SELECT 1"))
    except SQLAlchemyError:
        db.session.rollback()
        return error(
            "DATABASE_UNAVAILABLE",
            "A API está online, mas o banco SQLite não respondeu.",
            503,
        )

    return success({"status": "healthy", "database": "connected"})
