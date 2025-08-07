from fastapi import FastAPI

app = FastAPI()

# http://127.0.0.1:8000/

@app.get("/")
def index():
  return {"message": "Hy this is the FastAPI backend! Welcome!" }

@app.get("/users/{id}")
def mostrar_usuario(id: int):
  return {"data": id}