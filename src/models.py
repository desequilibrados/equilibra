from sqlalchemy import Column, Integer, String, Float
from src.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    objetivo = Column(String)
    peso_atual = Column(Float)