from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# http://127.0.0.1:8000/

class User(BaseModel):
    id: int
    name: str
    email: str
    editorial: Optional[str] 

@app.get("/")
def index():
  return {"message": "Hy this is the FastAPI backend! Welcome!" }

@app.get("/users/{id}")
def mostrar_usuario(id: int):
  return {"data": id}


@app.post("/users/")
def mostrar_usuario(user: User):
  return {"message": f"User: {user.name} is registred"}