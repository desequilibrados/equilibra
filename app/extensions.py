"""Extensões compartilhadas pela aplicação."""

from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# As instâncias são criadas sem app para suportar o application factory e os testes.
db = SQLAlchemy()
cors = CORS()
