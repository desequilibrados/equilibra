# Arquivo principal

from fastapi import FastAPI

# Inicializa o FastAPI com o título e descrição da API.
app = FastAPI(
    title="API Equilibra",
    description="API de Planejamento Alimentar",
)

# Inicializa a rota principal da API, que retorna uma mensagem de boas-vindas.
@app.get("/")
def home():
    return {"mensagem": "A API do Equilibra está online."}

# Removi a integração temporaria do banco antigo e deixei a API separada pra integração futura do SQLite.