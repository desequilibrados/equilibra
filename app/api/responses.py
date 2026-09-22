"""Padronização das respostas HTTP da API."""

from __future__ import annotations

from typing import Any

from flask import jsonify


def success(data: Any = None, message: str | None = None, status: int = 200):
    """Cria uma resposta de sucesso consistente."""

    payload: dict[str, Any] = {}
    if message is not None:
        payload["message"] = message
    if data is not None:
        payload["data"] = data
    return jsonify(payload), status


def error(code: str, message: str, status: int, details: Any = None):
    """Cria uma resposta de erro consistente e legível por clientes da API."""

    payload: dict[str, Any] = {
        "error": {
            "code": code,
            "message": message,
        }
    }
    if details is not None:
        payload["error"]["details"] = details
    return jsonify(payload), status
