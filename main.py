from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(
    title="API de Usuários Simples",
    description="Uma API simples para teste do FastAPI com operações CRUD",
    version="1.0.0"
)


class User (BaseModel):
    id:Optional[int] = None
    name: str
    email:str
    age: int


users_db = []
next_id = 1 

@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo à API de Usuários Simples",
        "endpoints": {
            "GET /users": "Lista todos os usuários",
            "GET /users/{id}": "Busca um usuário específico",
            "POST /users": "Cria um novo usuário",
            "PUT /users/{id}": "Atualiza um usuário existente"
        }
    }

@app.get("/users", response_model=List[User])
def get_all_users():
    return users_db


# GET - Buscar usuário por ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")


# POST - Criar novo usuário
@app.post("/users", response_model=User)
def create_user(user: User):
    global next_id
    user.id = next_id
    next_id += 1
    users_db.append(user)
    return user

# PUT - Atualizar usuário existente
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users_db):
        if user.id == user_id:
            # Mantém o ID original e atualiza outros campos
            updated_user.id = user_id
            users_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API está funcionando"}