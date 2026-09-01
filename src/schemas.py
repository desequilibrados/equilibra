from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    objetivo: str
    peso_atual: float