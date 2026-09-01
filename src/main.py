from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database import engine, Base, SessionLocal
from src import models, schemas


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Equilibra", 
    description="API de Planejamento Alimentar com auxilio de Inteligência Artificial",
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "A API do Equilibra está online."}

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

from src.ai_service import gerar_plano_alimentar

@app.post("/gerar-plano/")
def criar_plano_ia(objetivo: str, peso: float):
    plano = gerar_plano_alimentar(objetivo, peso)
    return {
        "objetivo": objetivo, 
        "peso_atual": peso, 
        "planejamento_ia": plano
    }