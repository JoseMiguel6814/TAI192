from fastapi import FastAPI, HTTPException
from typing import Optional



app=FastAPI(
    title='API de prueba 192',
    description='Jose Miguel Perusquia Hernandez',
    version='1.0.1'
    )

usuarios = [
    {"id":1, "nombre":"Juan","edad":25},
    {"id":2, "nombre":"Maria","edad":30},
    {"id":3, "nombre":"Pedro","edad":35},
    {"id":4, "nombre":"Jose","edad":40}
]

#endpoint home
@app.get("/",tags=["hola mundo"]) 
def home():
    return {"message": "Hello World"}




#endpoint Consultar Todos
@app.get("/todosusuarios",tags=["Operaciones Crud"])
def LeerUsuarios():
    return {"los usuarios son": usuarios}




#endpoint Agregar Usuario
@app.post("/agregarusuario",tags=["Operaciones Crud"])
def AgregarUsuario(usuario: dict):
    for usr in usuarios:
       if usr["id"] == usuario.get("id"):
           raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#endpoint put modificar usuario
@app.put("/modificarusuario/{id}",tags=["Operaciones Crud"])
def ModificarUsuario(id:int, nombre:str, edad:int):
    for usr in usuarios:
        if usr["id"] == id:
            usr["nombre"] = nombre
            usr["edad"] = edad
            return usuarios
           

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


#endpoint delete eliminar usuario
@app.delete("/eliminarusuario/{id}",tags=["Operaciones Crud"])
def EliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"message": "Usuario eliminado"}, usuarios
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    