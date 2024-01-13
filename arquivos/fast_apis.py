#pip install fastapi uvicorn[standard]
#uvicorn fast_apis:app --reload
#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/redoc
from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    id:int
    nome:str
    preco:float
    em_oferta: bool = False

app = FastAPI()

produtos = [
    Produto(id=1,nome="playstation 1",preco=100.20,em_oferta=True),
    Produto(id=2,nome="playstation 2",preco=1022.20,em_oferta=True),
    Produto(id=3,nome="playstation 3",preco=10330.20,em_oferta=True),
    Produto(id=4,nome="playstation 4",preco=14400.20,em_oferta=True),
]

@app.get('/')
async def index():
    return {"geek":"university"}

@app.get('/produtos/{id}')
async def buscar_produto(id:int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return 

@app.put('/produtos/{id}')
async def atualizar_produto(id:int,produto:Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return prod
        
    return None