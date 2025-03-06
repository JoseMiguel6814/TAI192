from fastapi import FastAPI, HTTPException,Depends
from typing import Optional, List
from pydantic import BaseModel
from modelsPydantics import ModeloUsuario, modeloAuth
from genToken import createToken
from fastapi.responses import JSONResponse
from middlewares import BearerJWT


app=FastAPI(
    title='API de prueba 192',
    description='Jose Miguel Perusquia Hernandez',
    version='1.0.1'
    )



#lista de usuarios

usuarios = [
    {"id":1, "nombre":"Juan","edad":25, "correo":"example@example.com"},
    {"id":2, "nombre":"Maria","edad":30,"correo":"example2@example.com"},
    {"id":3, "nombre":"Pedro","edad":35,"correo":"exampl3@example.com"},
    {"id":4, "nombre":"Jose","edad":40,"correo":"exampl4@example.com"}
]

#endpoint home
@app.get("/",tags=["hola mundo"]) 
def home():
    return {"message": "Hello World"}

#endpoint autenticacion
@app.post("/auth", tags=["Autentificacion"])
def login(autorizacion: modeloAuth):
   if autorizacion.email == "example@example.com" and autorizacion.passw == "12345678":
       token:str = createToken(autorizacion.model_dump())
       print(token)
       return JSONResponse(content={"token": token})
    

#endpoint Consultar Todos
@app.get("/todosusuarios",dependencies={Depends(BearerJWT())},response_model= List[ModeloUsuario], tags=["Operaciones Crud"])
def LeerUsuarios():
    return usuarios




#endpoint Agregar Usuario
@app.post("/agregarusuario", response_model= ModeloUsuario,  tags=["Operaciones Crud"])
def AgregarUsuario(usuario: ModeloUsuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
           raise HTTPException(status_code=400, detail="El usuario ya existe")
    usuarios.append(usuario)
    return usuario

#endpoint put modificar usuario
@app.put("/modificarusuario/{id}",response_model= ModeloUsuario,tags=["Operaciones Crud"])
def ModificarUsuario(id:int, usuario: ModeloUsuario):
    for usr in usuarios:
        if usr["id"] == id:
            usr["nombre"] = usuario.nombre
            usr["edad"] = usuario.edad
            usr["correo"] = usuario.correo
            return usuario
           

    raise HTTPException(status_code=404, detail="Usuario no encontrado")


#endpoint delete eliminar usuario
@app.delete("/eliminarusuario/{id}",tags=["Operaciones Crud"])
def EliminarUsuario(id:int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return {"message": "Usuario eliminado"}, usuarios
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
