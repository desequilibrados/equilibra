from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database import engine, Base, SessionLocal
from src import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Equilibra", 
    description="API para planejamento alimentar com IA"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "A API do Equilibra está no ar!"}

@app.post("/usuarios/")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = models.Usuario(
        nome=usuario.nome, 
        objetivo=usuario.objetivo, 
        peso_atual=usuario.peso_atual
    )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return {"mensagem": "Usuário cadastrado com sucesso!", "dados": novo_usuario}