# API do banco de dados - SQLite

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# create_engine = cria o gerenciador da conexão com o banco de dados
# sessionmaker = faz ser possivel cadastrar, consultar e etc.
# declarative_base = cria uma classe base para os modelos do SQLAlchemy.


SQLALCHEMY_DATABASE_URL = "sqlite:///./equilibra_banco.db" # Link pro banco hospedado localmente.

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
# O fastapi precisa do check_same_thread para funcionar com SQLite, pois ele não permite múltiplas threads acessando o mesmo banco de dados ao mesmo tempo.
)

SessionLocal = sessionmaker(
    autocommit=False, # Garante que é necessario confirmar as alterações no banco de dados antes de serem salvas.
    autoflush=False, # Garante que as alterações no banco de dados não sejam salvas automaticamente.
    bind=engine # Informa qual engine será usado para criar as sessões do banco de dados.
)

Base = declarative_base() 
# A classe base é usada para criar os modelos do SQLAlchemy, que são as classes que representam as tabelas do banco de dados.