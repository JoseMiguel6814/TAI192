from fastapi import FastAPI, HTTPException
from typing import Optional



app=FastAPI(
    title='API de prueba 192',
    description='Jose Miguel Perusquia Hernandez',
    version='1.0.1'
    )

TASKS = [
    {"id":1, "titulo":"Estudiar examen","descripcion": 25, "vencimiento": "12/12/12", "estado": "completada"},
    {"id":2, "titulo":"Hacer el PI","descripcion":30, "vencimiento": "12/12/12", "estado": "completada"},
    {"id":3, "titulo":"Lavar la ropa","descripcion":35, "vencimiento": "12/12/12", "estado": "completada"},
    {"id":4, "titulo":"Lavar los trastes","descripcion": 40, "vencimiento": "12/12/12", "estado": "completada"}
]

#endpoint home
@app.get("/",tags=["hola mundo"]) 
def home():
    return {"message": "Hello World"}


#endpoint Consultar Todas las tareas
@app.get("/todasTareas",tags=["Operaciones Crud"])
def LeerTareas():
    return {"las Tareas son": TASKS}

