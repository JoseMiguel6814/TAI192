from fastapi import FastAPI, HTTPException
from typing import Optional



app=FastAPI(
    title='API de prueba 192',
    description='Jose Miguel Perusquia Hernandez',
    version='1.0.1'
    )

TASKS = [
    {"id":1, "titulo":"Estudiar examen","descripcion": "estudiar para abracitos", "vencimiento": "12/12/12", "estado": "completada"},
    {"id":2, "titulo":"Hacer el PI","descripcion":"tengo que preguntarle a chat", "vencimiento": "12/12/12", "estado": "completada"},
    {"id":3, "titulo":"Lavar la ropa","descripcion":"ya no tengo ropa para manana ", "vencimiento": "12/12/12", "estado": "completada"},
    {"id":4, "titulo":"Lavar los trastes","descripcion": "mi mamam me va a reganar", "vencimiento": "12/12/12", "estado": "completada"}
]

#endpoint home
@app.get("/",tags=["hola mundo"]) 
def home():
    return {"message": "Hello World"}


#endpoint Consultar Todas las tareas
@app.get("/todasTareas",tags=["Operaciones Crud"])
def LeerTareas():
    return {"las Tareas son": TASKS}

#endpoint consultar una tarea por id
@app.get("/tarea/{id}",tags=["Operaciones Crud"])
def LeerTarea(id:int):
    for task in TASKS:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

#endpoint Agregar Tarea
@app.post("/agregarTarea",tags=["Operaciones Crud"])
def AgregarTarea(id:int, titulo:str, descripcion:str, vencimiento:str, estado:str):
    for task in TASKS:
        if task["id"] == id:
            raise HTTPException(status_code=400, detail="La tarea ya existe")
    TASKS.append({"id":id, "titulo":titulo, "descripcion": descripcion, "vencimiento": vencimiento, "estado": estado})
    return {"id":id, "titulo":titulo, "descripcion": descripcion, "vencimiento": vencimiento, "estado": estado}
   